"""Archive final continuation-state scratch without changing frozen review evidence."""
import hashlib,json,pathlib,shutil
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');root=pathlib.Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_174')
targets=[]
for n in ['163','170','173']:
 for f in sorted(w.iterdir()):
  if n not in f.name or f.name.endswith(('_progress.md','_cleanup.json')):continue
  if f.name.endswith(('-deferred-review','-source-review')):
   destination=root/'analysis/prior_candidate_reviews'/('case'+n)
  else:
   destination=root/'analysis/prior_candidate_reviews'/('case'+n+'_final_scratch')/f.name
   if f.is_dir():shutil.copytree(f,destination)
   else:destination.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,destination)
  files=[p for p in f.rglob('*')if p.is_file()]if f.is_dir()else[f]
  for p in files:
   d=destination/p.relative_to(f)if f.is_dir()else destination
   assert hashlib.sha256(p.read_bytes()).digest()==hashlib.sha256(d.read_bytes()).digest(),p
  targets.append({'source':str(f),'archive':str(destination),'files':len(files)})
(root/'analysis/creation_tools/deferred_cleanup_targets174.json').write_bytes((json.dumps(targets,ensure_ascii=False,indent=2)+'\n').encode())
shutil.copy2(w/'Dockerfile.spglib174-local',root/'analysis/creation_tools/Dockerfile.spglib174-local')
print('Archived final scratch for',len(targets),'exact targets; frozen inner manifests unchanged.')
