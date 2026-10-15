"""Record completed local verification without claiming unfinished publication."""
import datetime,json,shutil
from pathlib import Path
w=Path('E:/CLB_Swe-bench/_work/pyc_batch')
repo=Path('E:/CLB_Swe-bench/pyc-swebench');r=repo/'Y_test_data/pyc_case_081'
def put(path,text):
    with path.open('w',encoding='utf-8',newline='\n')as stream:stream.write(text)
def save(path,value):put(path,json.dumps(value,ensure_ascii=False,indent=2)+'\n')
pending=r/'verification/publication/engine-startup-blocker.json'
save(pending,json.loads(pending.read_text(encoding='utf-8')))
note='Publication is pending: formal verification and workbook checks passed, but Docker Desktop currently fails during sailor-ingest socket startup. Neither the 081 Docker Hub push nor Git remote push has been performed. The verified image and all original evidence are retained; cleanup waits until publication succeeds.'
for path in (r/'README.md',r/'verification/README.md'):
    text=path.read_text(encoding='utf-8')
    if note not in text:put(path,text.rstrip()+'\n\n## Publication status\n\n'+note+'\n')
readme=repo/'README.md';text=readme.read_text(encoding='utf-8')
lines=[]
for line in text.splitlines():
    if '| `pyc_case_081`' in line and 'publication pending' not in line:line=line.rstrip().rstrip('|').rstrip()+'; publication pending Docker recovery |'
    lines.append(line)
put(readme,'\n'.join(lines)+'\n')
spec=json.loads((w/'case081_spec.json').read_text(encoding='utf-8'));spec['publicationStatus']='pending_docker_engine_recovery';save(w/'case081_spec.json',spec)
metadata=json.loads((r/'official_swebench/metadata.json').read_text(encoding='utf-8'))
metadata['publication']={'status':'pending_docker_engine_recovery','image_push_performed':False,'git_push_performed':False,'evidence':'verification/publication/engine-startup-blocker.json'}
save(r/'official_swebench/metadata.json',metadata)
batchPath=w/'batch_state.json';batch=json.loads(batchPath.read_text(encoding='utf-8'))
for item in batch['candidates']:
    if item['caseNumber']=='081':
        item.update(status='verified_publication_pending_docker',baseCommit=spec['baseCommit'],image=spec['image'],note=note,updatedAt=datetime.datetime.now(datetime.timezone.utc).isoformat())
    elif item['caseNumber']=='078':item['evidence']='E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_081/analysis/prior_candidate_reviews/case078/deferral.json'
save(batchPath,batch)
put(w/'case081_progress.md','# Case081: verified_publication_pending_docker\n\n'+note+'\n\nGold resolved with4passes; negative1fail3pass; test conflict rejected. Exact C product723bytes/test1496bytes, typed workbook dates2018-12-30/31 and four IDs checked. Prior078 no_base_failure evidence is retained under081 analysis/prior_candidate_reviews. Build-only missing font and Docker RPC EOF histories are preserved. Final resource-complete environment uses fixed tracked default font, native1.9.5.dev0/FreeType2.10.4/SDL2.0.14/X11.\n\nNext: restore Docker Engine externally, run audit_publication081.mjs, explicit direct fixed081image push, record_publication081.mjs, refresh/finalize/verify, actual committed blob checks, direct Git push/remote confirmation, prototype removal and exact archived-byte cleanup; only then mark published_cleaned. No next candidate started.\n')
shutil.copyfile(w/'checkpoint_case081.py',r/'analysis/creation_tools/checkpoint_case081.py')
print('081 verified local package checkpointed; publication and cleanup explicitly pending.')
