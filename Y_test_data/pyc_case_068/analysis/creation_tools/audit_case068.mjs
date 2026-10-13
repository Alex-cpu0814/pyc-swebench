import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
const work='E:/CLB_Swe-bench/_work/pyc_batch',s=JSON.parse(fs.readFileSync(work+'/case068_spec.json','utf8'));
const formal=process.argv.includes('--formal'),out=formal?'E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_068/verification/runtime-audit':work+'/case068-runtime-audit';
fs.mkdirSync(out);
const files=['Images/lena.ppm','Images/lena.jpg','PIL/Image.py','_imaging.c','libImaging/Quant.c','libImaging/QuantOctree.c'];
const code=`import PIL,json,hashlib,pathlib; from PIL import Image; files=${JSON.stringify(files)}; report={"pillow_version":PIL.PILLOW_VERSION,"pillow_file":PIL.__file__,"core_version":Image.core.PILLOW_VERSION,"core_file":Image.core.__file__,"core_sha256":hashlib.sha256(pathlib.Path(Image.core.__file__).read_bytes()).hexdigest(),"jpeg_support":hasattr(Image.core,"jpeg_decoder"),"zlib_support":hasattr(Image.core,"zip_decoder"),"assets":{p:{"size":pathlib.Path(p).stat().st_size,"sha256":hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()} for p in files}}; assert report["pillow_version"]==report["core_version"]=="2.3.0"; assert report["jpeg_support"] and report["zlib_support"]; assert all(report[k].startswith("/testbed/PIL/") for k in ("pillow_file","core_file")); Image.open("Images/lena.ppm").load(); Image.open("Images/lena.jpg").load(); print(json.dumps(report))`;
let cmd=`set -euo pipefail; test "$(git rev-parse HEAD)" = "${s.baseCommit}"; test -z "$(git status --porcelain)"; `;
for(const [file,blob] of Object.entries(s.provenance.baseline_asset_git_blobs))cmd+=`test "$(git hash-object ${file})" = "${blob}"; `;
cmd+=`dpkg-query -W gcc libjpeg62-turbo-dev zlib1g-dev libfreetype6-dev libopenjp2-7-dev libtiff-dev; python -c '${code}'`;
const image=formal?s.image:s.prototypeImage,args=['run','--rm','--network','none','--entrypoint','/bin/bash',image,'-lc',cmd],startedAt=new Date().toISOString();
const r=spawnSync('C:/Users/玉兔/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe',args,{encoding:'utf8',timeout:120000,windowsHide:true,maxBuffer:5*1024*1024});
fs.writeFileSync(out+'/stdout.raw.log',r.stdout??'');fs.writeFileSync(out+'/stderr.raw.log',r.stderr??'');
const packages={};let audit=null;for(const line of (r.stdout??'').split('\n')){const p=line.trim().split('\t');if(p.length===2)packages[p[0].replace(/:amd64$/,'')]=p[1];if(line.startsWith('{'))audit=JSON.parse(line);}
const summary={startedAt,finishedAt:new Date().toISOString(),image,exitCode:r.status,error:r.error?.message??null,native_package_versions:packages,runtime_audit:audit,command:args};
fs.writeFileSync(out+'/summary.json',JSON.stringify(summary,null,2)+'\n');console.log(JSON.stringify({exitCode:r.status,error:summary.error,audit}));process.exitCode=r.status??1;
