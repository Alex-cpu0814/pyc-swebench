import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
const work='E:/CLB_Swe-bench/_work/pyc_batch',p=work+'/case070_spec.json',s=JSON.parse(fs.readFileSync(p,'utf8'));
for(const [label,exit] of [['base',1],['gold',0]]){
 const dir=work+'/case070-probe-'+label,a=JSON.parse(fs.readFileSync(dir+'/summary.json','utf8')),log=fs.readFileSync(dir+'/stdout.raw.log','utf8');
 if(a.exitCode!==exit||a.error)throw new Error('Unverified '+label);
 for(const node of s.probeNodes){const expected=label==='base'&&s.failToPass.includes(node)?'FAILED':'PASSED';if(!log.split('\n').some(x=>x.startsWith(node+' ')&&x.includes(expected)))throw new Error(node+' '+expected);}
}
const audit=JSON.parse(fs.readFileSync(work+'/case070-runtime-audit/summary.json','utf8'));
if(audit.exitCode!==0||audit.runtime_audit.ujson_version!==s.version)throw new Error('Runtime version not verified');
s.validationStatus='verified_base_gold';
s.verifiedError='Base fails the exact official test_encode_indent assertion: ujson.encode(obj, indent=4) emits one leading space instead of the expected four spaces. Native PyArg_ParseTupleAndKeywords parses indent using boolean format p, collapsing nonzero integer4 to1. Gold changes that format to integer i and passes the target plus all three unchanged dict/list encoding and Unicode decoding regressions. No skipped or missing nodes, process termination or instrumentation observed.';
s.verifiedError=s.verifiedError.replace('integer4 to1','integer 4 to 1');
s.targetSummary='Base: 1 official indentation target fails and 3 regressions pass. Gold: all 4 official nodes pass.';
s.verifiedTest=[...s.failToPass,...s.passToPass].join(' and ');
s.testScope='The exact protected upstream test decodes the JSON object {"obj":31337} and compares its indent=4 encoded text with the original four-space formatting. Three unchanged official regressions cover ordinary dictionary/list conversion and Unicode decoding. Tests execute normally in one pytest process, without altered values, assertions or thresholds. Product patch is the single native C argument-format change; vendored C++ double-conversion is compiled but unchanged.';
s.provenance.formal_prototype_runtime_audit={runtime:audit.runtime_audit,native_package_versions:audit.native_package_versions};
const git=args=>{const r=spawnSync('git',['-C',s.sourceRepo,...args],{encoding:'utf8'});if(r.status!==0&&r.status!==1)throw new Error(r.stderr);return r;};
function control(file,transform){const before=git(['show',s.baseCommit+':'+file]).stdout,after=transform(before);if(before===after)throw new Error('Unchanged control');const a=work+'/case070-control-before.txt',b=work+'/case070-control-after.txt';fs.writeFileSync(a,before);fs.writeFileSync(b,after);return git(['diff','--no-index','--',a,b]).stdout.replace(/^diff --git .*$/m,'diff --git a/'+file+' b/'+file).replace(/^--- .*$/m,'--- a/'+file).replace(/^\+\+\+ .*$/m,'+++ b/'+file);}
s.negativePatch=control('README.rst',x=>x.replace('UltraJSON\n=========\n','UltraJSON\n=========\n\nThe negative control leaves integer indentation parsing unchanged.\n'));
s.tamperPatch=control('tests/test_ujson.py',x=>x.replace('def test_decode_from_unicode():','def test_decode_from_unicode_tamper():'));
fs.writeFileSync(p,JSON.stringify(s,null,2)+'\n');
fs.appendFileSync(work+'/case070_progress.md','\n'+new Date().toISOString()+' Prototype Base1 failure/3passes, Gold4passes. Actual indent4 output one space instead of four; C p->i parser repair. Runtime and SCM3.2.1.dev2 verified from fixed tag/history and vendored source. Formal controls pending.\n');
console.log(s.targetSummary);
