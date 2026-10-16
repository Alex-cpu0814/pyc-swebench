import fs from'node:fs';
const w='E:/CLB_Swe-bench/_work/pyc_batch',h=fs.readFileSync(w+'/case128_pr200.raw.html','utf8'),found=[];
for(const m of h.matchAll(/<script type="application\/json"[^>]*data-target="[^"]*embeddedData"[^>]*>(.*?)<\/script>/gs)){
 const obj=JSON.parse(m[1]);function walk(o,p=''){if(!o||typeof o!=='object')return;for(const[k,v]of Object.entries(o)){const key=p+'.'+k;if(v&&typeof v==='object')walk(v,key);else if(/(createdAt|created_at|mergedAt|merged_at|pullRequestNumber|number|mergeCommit|merged)$/.test(k))found.push({path:key,value:v});}}walk(obj);
}
fs.writeFileSync(w+'/case128_html_structured_dates.json',JSON.stringify(found,null,2)+'\n');console.log(JSON.stringify(found));
