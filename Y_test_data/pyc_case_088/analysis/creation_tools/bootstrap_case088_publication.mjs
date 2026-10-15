import fs from 'node:fs';
const w='E:/CLB_Swe-bench/_work/pyc_batch',prev='E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_086/analysis/creation_tools';
for(const name of ['audit_publication086.mjs','record_publication086.mjs','verify_committed_case086.mjs']){
 let t=fs.readFileSync(prev+'/'+name,'utf8').replaceAll('086','088').replaceAll('SDL2/companion','SDL1.2/companion');
 if(name==='record_publication086.mjs'){
  t=t.replace("if(digest!=='sha256:11e605344ed4675be7b010289e782843d09aa9efc3fae6d819d905c65ab7a0f3')throw new Error('Push digest missing/mismatched');","if(!digest)throw new Error('Push digest missing');");
  t=t.replace("if(local.Id!==digest||!local.RepoDigests.includes(s.image.split(':')[0]+'@'+digest))throw new Error('Published image changed');","const gold=JSON.parse(fs.readFileSync(root+'/verification/runs/case-088-final-gold/summary.json','utf8')); if(local.Id!==gold.image.id||!local.RepoDigests.includes(s.image.split(':')[0]+'@'+digest))throw new Error('Published image changed'); if(local.Descriptor?.digest && local.Descriptor.digest!==digest)throw new Error('OCI descriptor mismatch');");
 }
 fs.writeFileSync(w+'/'+name.replaceAll('086','088'),t);
}
console.log('088 direct publication audit, result capture and committed-blob verification tools prepared.');
