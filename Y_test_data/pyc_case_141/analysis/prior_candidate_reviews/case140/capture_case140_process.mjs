import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
const root='E:/CLB_Swe-bench/_work/pyc_batch/case140-process-observation';
fs.mkdirSync(root,{recursive:false});
const docker='C:/Users/玉兔/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe';
const id='da98fed50a11';
for(const [name,args] of [['inspect',['inspect',id]],['logs',['logs',id]],['top',['top',id,'-eo','pid,ppid,stat,comm,args']]]){
 const startedAt=new Date().toISOString();
 const r=spawnSync(docker,args,{encoding:'utf8',timeout:30000,maxBuffer:8*1024*1024});
 fs.writeFileSync(`${root}/${name}.stdout.raw.log`,r.stdout??'');
 fs.writeFileSync(`${root}/${name}.stderr.raw.log`,r.stderr??'');
 fs.writeFileSync(`${root}/${name}.summary.json`,JSON.stringify({startedAt,finishedAt:new Date().toISOString(),command:[docker,...args],exitCode:r.status,signal:r.signal,error:r.error?.message??null},null,2)+'\n');
 if(r.status!==0)throw Error(name+' capture failed');
}
console.log(root);
