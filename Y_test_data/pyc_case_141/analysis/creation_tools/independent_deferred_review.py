"""Read-only archive and exact upstream patch review for deferred candidates."""
import hashlib,json,pathlib,subprocess,sys
sys.dont_write_bytecode=True
root=pathlib.Path(sys.argv[1]);source=pathlib.Path(sys.argv[2])
decision=json.loads((root/'decision.json').read_text(encoding='utf-8'))
base,fix=decision['base_commit'],decision['fix_commit']
changed=subprocess.check_output(['git','-C',str(source),'diff','--name-only',base,fix],text=True).splitlines()
assert set(changed)==set(decision['product_files']+decision['test_files'])
for name,files in [('complete',None),('product',decision['product_files']),('test',decision['test_files'])]:
    command=['git','-C',str(source),'diff',base,fix]+(['--']+files if files is not None else [])
    assert subprocess.check_output(command)==(root/f'{name}_patch.diff').read_bytes(),name
manifest=root/'SHA256SUMS.txt';raw=manifest.read_bytes();assert b'\r'not in raw and b'\\n'not in raw
entries=[line.split('  ',1)for line in raw.decode().splitlines()];paths=[path for digest,path in entries]
assert len(paths)==len(set(paths))
assert set(paths)=={p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p!=manifest}
for digest,path in entries:assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,path
print(json.dumps({'case':decision['case_number'],'status':decision['status'],'complete_upstream_files':changed,'archive_hashes':len(entries),'review':'independent_exact_patches_and_archive_verified'}))
