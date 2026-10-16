"""Read-only second review of delivered benchmark evidence and committed bytes."""
import sys
sys.dont_write_bytecode=True
import argparse,datetime,hashlib,importlib.util,json,pathlib,re,subprocess,xml.etree.ElementTree as ET,zipfile

parser=argparse.ArgumentParser();parser.add_argument('number');parser.add_argument('--hashes',action='store_true');parser.add_argument('--committed',action='store_true');args=parser.parse_args()
assert len(args.number)==3 and args.number.isdigit()
repo=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench');root=repo/f'Y_test_data/pyc_case_{args.number}'
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
spec=read(root/f'analysis/creation_tools/case{args.number}_spec.json')
instance=read(root/f'official_swebench/instance_{args.number}.json');meta=read(root/'official_swebench/metadata.json')
nodes=instance['FAIL_TO_PASS']+instance['PASS_TO_PASS'];assert len(nodes)==len(set(nodes)) and set(nodes)==set(spec['probeNodes'])
for kind,key,files in [('gold','patch',meta['product_files']),('test','test_patch',meta['test_files'])]:
    command=['git','-C',spec['sourceRepo'],'diff']+(['--binary']if spec.get('binaryPatches')else[])+[spec['baseCommit'],spec['fixCommit'],'--']+files
    upstream=subprocess.check_output(command)
    assert upstream==(root/f'patches/{kind}_patch.diff').read_bytes(),kind
    assert instance[key].encode()==upstream,kind

modulePath=root/'evaluator/evaluate_model_patch.py';sys.path.insert(0,str(modulePath.parent));moduleSpec=importlib.util.spec_from_file_location('independent_evaluator',modulePath);module=importlib.util.module_from_spec(moduleSpec);moduleSpec.loader.exec_module(module)
imageIds=set();outcomes={}
for label in ['gold','negative','tamper']:
    directory=root/f'verification/runs/case-{args.number}-final-{label}';summary=read(directory/'summary.json');imageIds.add(summary['image']['id'])
    if label=='tamper':assert summary['reason']=='candidate_conflicts_with_test_patch'
    else:
        assert summary['status']==('resolved'if label=='gold'else'unresolved')
        expectedExit=0 if label=='gold'else spec.get('expectedBaseExitCode',1)
        assert summary['phase']['test_exit_code']==expectedExit
        rawTests=(directory/'tests.raw.log').read_text(encoding='utf-8')
        observed=module.parse_test_log(rawTests);grading=read(directory/'grading.json')
        nativeMissing=label=='negative'and expectedExit in (134,139,-6,-11)
        if nativeMissing:
            assert len(instance['FAIL_TO_PASS'])==1,'A process-level native exit cannot prove multiple uncompleted targets'
            target=instance['FAIL_TO_PASS'][0]
            assert re.search(r'^'+re.escape(target)+r'(?:\s|$)',rawTests,re.M),'Native target must actually start'
            assert re.search(r'\b(?:Aborted|Segmentation fault)\b|Fatal Python error',rawTests),'Native exit must have original raw evidence'
            assert target not in observed,'Preserve absent terminal result rather than inventing FAILED'
        expected={n:(('MISSING'if nativeMissing else spec.get('expectedBaseNodeStatuses',{}).get(n,'FAILED'))if label=='negative'and n in instance['FAIL_TO_PASS']else'PASSED')for n in nodes}
        assert observed=={n:s for n,s in expected.items()if s!='MISSING'},(label,observed)
        assert expected=={**grading['FAIL_TO_PASS'],**grading['PASS_TO_PASS']},(label,grading)
    outcomes[label]=summary['reason']
assert len(imageIds)==1
namespace={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(root/f'analysis/source_material/single_pyc_case_{args.number}.xlsx')as book:
    assert [s.attrib['name']for s in ET.fromstring(book.read('xl/workbook.xml')).find('m:sheets',namespace)]==['Source Record','SWE-bench Record']
    shared=[]
    if 'xl/sharedStrings.xml'in book.namelist():shared=[''.join(s.itertext())for s in ET.fromstring(book.read('xl/sharedStrings.xml'))]
    for index in [1,2]:
        cells={}
        for cell in ET.fromstring(book.read(f'xl/worksheets/sheet{index}.xml')).findall('.//m:c',namespace):
            assert cell.attrib.get('t')!='e'
            value=cell.find('m:v',namespace);inline=cell.find('m:is',namespace)
            text=value.text if value is not None else ''.join(inline.itertext())if inline is not None else None
            cells[cell.attrib['r']]=shared[int(text)]if cell.attrib.get('t')=='s'else text
    rows=sorted((int(address[1:]),value)for address,value in cells.items()if address.startswith('A')and address[1:].isdigit())
    assert [cells.get(f'B{index}')for index,label in rows if label and(label.startswith('FAIL_TO_PASS (')or label.startswith('PASS_TO_PASS ('))]==nodes
    if spec.get('workbookDateFields'):
        for label,key in [('Created at','createdAt'),('Merged at','mergedAt')]:
            values=[cells.get(f'B{index}')for index,text in rows if text==label]
            if spec.get(key):
                assert len(values)==1,(label,values)
                assert(datetime.datetime(1899,12,30)+datetime.timedelta(days=float(values[0]))).date().isoformat()==spec[key]
            else:
                assert not values or values==[None]or values==[''],(label,'unknown date must be absent or blank',values)

count=None;head=None
if args.hashes or args.committed:
    sums=root/'official_swebench/SHA256SUMS.txt';raw=sums.read_bytes();assert b'\r'not in raw and b'\\n'not in raw
    entries=[line.split('  ',1)for line in raw.decode().splitlines()];paths=[p for h,p in entries];assert len(paths)==len(set(paths))
    actual={p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p!=sums};assert actual==set(paths),(actual-set(paths),set(paths)-actual)
    for digest,path in entries:assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,path
    count=len(entries)
    if args.committed:
        request=''.join(f'HEAD:Y_test_data/pyc_case_{args.number}/{path}\n'for digest,path in entries).encode();blobs=subprocess.check_output(['git','-C',str(repo),'cat-file','--batch'],input=request);position=0
        for digest,path in entries:
            end=blobs.index(b'\n',position);header=blobs[position:end].split();assert len(header)==3,(path,header)
            size=int(header[2]);start=end+1;assert hashlib.sha256(blobs[start:start+size]).hexdigest()==digest,path;position=start+size+1
        head=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
print(json.dumps({'case':args.number,'official_nodes':len(nodes),'fail_to_pass':len(instance['FAIL_TO_PASS']),'pass_to_pass':len(instance['PASS_TO_PASS']),'formal_outcomes':outcomes,'image_id':next(iter(imageIds)),'saved_workbook':'two sheets/exact IDs/dates/no errors','local_hashes':count,'committed_head':head,'status':'independent_review_passed'}))
