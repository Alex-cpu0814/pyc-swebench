import fs from'node:fs';const w='E:/CLB_Swe-bench/_work/pyc_batch',r='E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_090';
// These are newly serialized HTTP metadata containers, not original raw logs.
// Response status, headers and escaped body bytes remain exactly represented.
for(const n of fs.readdirSync(w).filter(n=>n.startsWith('case090_')&&n.endsWith('.unavailable.json'))){const p=w+'/'+n,t=fs.readFileSync(p,'utf8').replaceAll('\r\n','\n');fs.writeFileSync(p,t);for(const d of ['analysis/creation_tools','analysis/source_material'])fs.copyFileSync(p,r+'/'+d+'/'+n);}
console.log('Generated API metadata serialized with LF; raw HTML and original build/test logs untouched.');
