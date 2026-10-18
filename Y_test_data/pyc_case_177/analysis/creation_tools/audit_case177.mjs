import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
const w='E:/CLB_Swe-bench/_work/pyc_batch',p=w+'/case177_spec.json',s=JSON.parse(fs.readFileSync(p,'utf8')),formal=process.argv.includes('--formal');
const out=formal?'E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_177/verification/runtime-audit':w+'/case177-runtime-audit';fs.mkdirSync(out);
const code=`from __future__ import print_function
import glob,hashlib,json,os,re,subprocess,sys
import jpy,jpyutil
assert sys.version_info[:2]==(2,7)
assert os.path.realpath(jpy.__file__).startswith('/testbed/') and jpy.__file__.endswith('.so')
jpyutil.init_jvm();assert jpy.has_jvm()
files=['src/main/c/jpy_jmethod.c', 'src/main/c/jpy_jtype.c', 'src/main/c/jpy_jtype.h', 'setup.py', 'README.md', 'src/test/python/jpy_overload_test.py']+[jpy.__file__]+sorted(glob.glob('target/test-classes/org/jpy/fixtures/*.class'))
version=re.search('__version__ = "([^"]+)"',open('setup.py').read()).group(1);assert version=='0.8-SNAPSHOT'
report={'package_version':version,'version_source':'exact upstream setup.py','python_version':sys.version,'module_path':jpy.__file__,'has_jvm':jpy.has_jvm(),'java_version':subprocess.check_output(['java','-version'],stderr=subprocess.STDOUT),'compiler':subprocess.check_output(['gcc','--version']).splitlines()[0],'measured_language_path':'original Python unittest -> compiled C/JNI extension -> OpenJDK8 JVM','assets':{f:{'size':os.path.getsize(f),'sha256':hashlib.sha256(open(f,'rb').read()).hexdigest()}for f in files}}
assert '1.8.0' in report['java_version'];assert len(files)>5
print(json.dumps(report))`;
const quote=v=>"'"+v.replaceAll("'","'\\''")+"'";
let cmd=`set -euo pipefail; test "$(git rev-parse HEAD)" = "${s.baseCommit}"; test -z "$(git status --porcelain)"; test -z "$(git remote)"; `;
for(const[f,b]of Object.entries(s.provenance.native_source_git_blobs))cmd+=`test "$(git hash-object ${f})" = "${b}"; `;
cmd+=`dpkg-query -W libc6 gcc g++ git python2.7 python2.7-dev openjdk-8-jdk-headless; ldd /testbed/src/main/python/jpy.so; python2.7 -c ${quote(code)}`;
const image=formal?s.image:s.prototypeImage,command=['run','--rm','--network','none','--entrypoint','/bin/bash',image,'-lc',cmd];
const r=spawnSync('C:/Users/玉兔/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe',command,{timeout:45000,maxBuffer:6*1024*1024});
fs.writeFileSync(out+'/stdout.raw.log',r.stdout??Buffer.alloc(0));fs.writeFileSync(out+'/stderr.raw.log',r.stderr??Buffer.alloc(0));
let report=null;const packages={};for(const line of(r.stdout??Buffer.alloc(0)).toString().split('\n')){const a=line.split('\t');if(a.length===2&&!line.startsWith('\t'))packages[a[0].replace(':amd64','')]=a[1];if(line.startsWith('{'))report=JSON.parse(line);}
fs.writeFileSync(out+'/summary.json',JSON.stringify({image,exitCode:r.status,error:r.error?.message??null,native_package_versions:packages,runtime_audit:report,source_git_identity:{base_commit:s.baseCommit,remotes_removed:r.status===0},command},null,2)+'\n');
if(r.status!==0||!report)throw Error((r.stderr??'').toString()||'Native audit report absent');
if(!formal){s.provenance.native_package_versions=packages;fs.writeFileSync(p,JSON.stringify(s,null,2)+'\n');}
console.log(JSON.stringify({image,exitCode:r.status,module:report.module_path,python:report.python_version,java:report.java_version}));
