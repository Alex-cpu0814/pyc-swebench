import fs from 'node:fs';import {spawnSync} from 'node:child_process';
const work='E:/CLB_Swe-bench/_work/pyc_batch',s=JSON.parse(fs.readFileSync(work+'/case056_spec.json','utf8')),formal=process.argv.includes('--formal');
const image=formal?s.image:s.prototypeImage,out=formal?'E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_056/verification/dependency-audit':work+'/case056-dependency-audit';
fs.mkdirSync(out);
const cmd=`set -euo pipefail; test "$(git rev-parse HEAD)" = "${s.baseCommit}"; test -z "$(git status --porcelain)"; dpkg-query -W gcc libjpeg62-turbo-dev zlib1g-dev libfreetype6-dev libopenjp2-7-dev libtiff-dev; python -c 'import PIL,json; from PIL import features; required=("jpg_2000","jpg","libtiff"); checks={x:features.check(x) for x in required}; assert all(checks.values()); print(json.dumps({"pillow_version":PIL.__version__,"pillow_file":PIL.__file__,"codec_support":checks,"codec_versions":{x:features.version(x) for x in required}}))'`;
const args=['run','--rm','--network','none','--entrypoint','/bin/bash',image,'-lc',cmd],startedAt=new Date().toISOString();
const r=spawnSync('C:/Users/玉兔/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe',args,{encoding:'utf8',timeout:120000,windowsHide:true});
fs.writeFileSync(out+'/stdout.raw.log',r.stdout??'');fs.writeFileSync(out+'/stderr.raw.log',r.stderr??'');
const packages={};let codecs=null;for(const line of (r.stdout??'').split('\n')){const parts=line.trim().split('\t');if(parts.length===2)packages[parts[0].replace(/:amd64$/,'')]=parts[1];if(line.startsWith('{'))codecs=JSON.parse(line);}
const summary={startedAt,finishedAt:new Date().toISOString(),image,exitCode:r.status,error:r.error?.message??null,command:args,native_package_versions:packages,codec_audit:codecs};
fs.writeFileSync(out+'/summary.json',JSON.stringify(summary,null,2)+'\n');console.log(JSON.stringify(summary,null,2));process.exitCode=r.status;
