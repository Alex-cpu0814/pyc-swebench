import fs from 'node:fs';
const w='E:/CLB_Swe-bench/_work/pyc_batch',old='E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_090/analysis/creation_tools/cleanup_case090.ps1';
let t=fs.readFileSync(old,'utf8').replaceAll('090','091').replaceAll('case091-prototype-build-v2','case091-prototype-build');
fs.writeFileSync(w+'/cleanup_case091.ps1',t);
console.log('091 scoped hash-before-delete scratch cleanup helper prepared.');
