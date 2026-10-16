import json,pathlib,shutil
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch').resolve()
for name in ['case157-prototype-build','case157-probe-base','case157-probe-gold','case157-probe-collect','case157-runtime-audit']:
 source=(w/name).resolve();dest=(w/name.replace('case157-','case157-initial-',1)).resolve()
 assert source.is_relative_to(w)and dest.is_relative_to(w)and source.exists()and not dest.exists()
 if name=='case157-prototype-build':shutil.copy2(w/'build_case157_prototype.mjs',source/'initial-build-helper.mjs')
 shutil.move(str(source),str(dest))
p=w/'build_case157_prototype.mjs';text=p.read_text(encoding='utf-8').replace("const cmd=['build','--progress=plain','-t',s.prototypeImage,context]","const cmd=['build','--platform',s.architecture,'--progress=plain','-t',s.prototypeImage,context]");p.write_bytes(text.encode())
(w/'case157-platform-correction.json').write_bytes((json.dumps({'observed':'The original FROM --platform=linux/386 build succeeded and its native audit inside build measured32-bit Python and long operand; docker image inspect also reported386. However explicit docker run --platform linux/386 could not find a matching local image variant and tried to pull the local-only tag. All3 initial probes exited125 before any test ran. Initial runtime audit likewise failed before audit execution.','correction':'Pass --platform linux/386 explicitly to docker build as well as FROM/run so exported OCI index and target platform agree. Preserve initial build/probe/audit evidence; rebuild with cached unchanged source/dependencies/tests/compile flags, then run original fixed node selection.','scope':'Build/export platform metadata correction; no original product/test/compiler/allocator changes and no tests selected by outcomes.'},indent=2)+'\n').encode())
print('Initial platform failure preserved; explicit build target configured.')
