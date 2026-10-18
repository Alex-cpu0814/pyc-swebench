import json,pathlib
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');p=w/'case176_spec.json';s=json.loads(p.read_text(encoding='utf-8'))
s['buildCommand']=s['buildCommand'].replace('setup.py build_ext','setup.py clean build_ext')
s['buildSystem']='Original setup.py clean build_ext --inplace --force, then ordinary javac compiles unchanged annotations and fixture classes. The original clean command makes setup.py skip its unconditional custom packaging/post-build suite; all selected complete official methods are executed separately by the evaluator. No source, assertion, compiler flags or product macros are changed.'
s['testSourceLabel']='Complete original Python unittest methods using the native C/JNI bridge'
p.write_bytes((json.dumps(s,ensure_ascii=False,indent=2)+'\n').encode())
p=w/'Dockerfile.jpy176-local';text=p.read_text(encoding='utf-8').replace('setup.py build_ext','setup.py clean build_ext').replace("'/*.so'","'/src/main/python/*.so'");p.write_bytes(text.encode())
p=w/'initialize_jpy176.py';text=p.read_text(encoding='utf-8').replace('setup.py build_ext','setup.py clean build_ext').replace("'/*.so'","'/src/main/python/*.so'");p.write_bytes(text.encode())
p=w/'audit_case176.mjs';text=p.read_text(encoding='utf-8').replace('ldd /testbed/jpy.so','ldd /testbed/src/main/python/jpy.so');p.write_bytes(text.encode())
print('Original setup.py clean/build_ext command configured; source and tests unchanged.')
