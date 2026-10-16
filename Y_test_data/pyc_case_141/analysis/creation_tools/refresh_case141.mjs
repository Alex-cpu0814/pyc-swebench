import fs from 'node:fs';
const w='E:/CLB_Swe-bench/_work/pyc_batch',r='E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_141',p=w+'/case141_spec.json',s=JSON.parse(fs.readFileSync(p,'utf8'));
for(const n of fs.readdirSync(w).filter(n=>n.includes(s.caseNumber)&&/\.(mjs|py|ps1)$/.test(n)))fs.copyFileSync(w+'/'+n,r+'/analysis/creation_tools/'+n);
const paths=[];function walk(d=''){for(const e of fs.readdirSync(r+(d?'/'+d:''),{withFileTypes:true})){const rel=(d?d+'/':'')+e.name;if(e.isDirectory()){if(e.name==='__pycache__')throw Error('Unarchived Python cache');walk(rel);}else if(rel!=='official_swebench/SHA256SUMS.txt')paths.push(rel);}}walk();
s.additionalVerificationAssets=[...new Set(paths)].sort();fs.writeFileSync(p,JSON.stringify(s,null,2)+'\n');fs.copyFileSync(p,r+'/analysis/creation_tools/case141_spec.json');console.log('Complete coverage '+paths.length);
