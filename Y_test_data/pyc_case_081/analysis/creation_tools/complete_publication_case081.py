"""Update the preserved local checkpoint after the exact image push succeeds."""
import json,shutil
from pathlib import Path
w=Path('E:/CLB_Swe-bench/_work/pyc_batch');repo=Path('E:/CLB_Swe-bench/pyc-swebench');r=repo/'Y_test_data/pyc_case_081'
def save(path,value):
    with path.open('w',encoding='utf-8',newline='\n')as f:json.dump(value,f,ensure_ascii=False,indent=2);f.write('\n')
publication=json.loads((r/'verification/publication/publication.json').read_text(encoding='utf-8'))
assert publication['registry_digest']=='sha256:4e5d69e396505fea954f28acb59dc90ef522bafab05dd484c0299e628f938720'
recoveryPath=r/'verification/publication/engine-recovery.json';recovery=json.loads(recoveryPath.read_text(encoding='utf-8'));assert recovery['status']=='engine_recovered';save(recoveryPath,recovery)
blockerPath=r/'verification/publication/engine-startup-blocker.json';blocker=json.loads(blockerPath.read_text(encoding='utf-8'));blocker.update(status='historical_engine_startup_blocker_resolved',resolved_evidence='verification/publication/engine-recovery.json',current_image_push_performed=True);save(blockerPath,blocker)
note='The exact verified image was successfully pushed to Docker Hub after Docker Engine recovered. Digest: '+publication['registry_digest']+'. Original startup failures and the data-preserving recovery are retained under verification/publication. Git remote confirmation and final cleanup are recorded in the batch progress after the source commit is published.'
for path in (r/'README.md',r/'verification/README.md'):
    text=path.read_text(encoding='utf-8').split('\n## Publication status\n')[0].rstrip()+'\n\n## Publication status\n\n'+note+'\n'
    with path.open('w',encoding='utf-8',newline='\n')as f:f.write(text)
readme=repo/'README.md';text=readme.read_text(encoding='utf-8').replace('; publication pending Docker recovery','')
with readme.open('w',encoding='utf-8',newline='\n')as f:f.write(text)
metadataPath=r/'official_swebench/metadata.json';metadata=json.loads(metadataPath.read_text(encoding='utf-8'));metadata['publication']={'status':'image_published_source_ready','registry_digest':publication['registry_digest'],'evidence':'verification/publication/publication.json','engine_recovery':'verification/publication/engine-recovery.json','git_remote_verification':'Recorded after source push in batch_state.json and case081_progress.md'};save(metadataPath,metadata)
specPath=w/'case081_spec.json';spec=json.loads(specPath.read_text(encoding='utf-8'));spec['publicationStatus']='image_published_source_ready';save(specPath,spec)
shutil.copyfile(w/'complete_publication_case081.py',r/'analysis/creation_tools/complete_publication_case081.py')
print('Image push recorded; historical startup blocker resolved; source ready for final commit.')
