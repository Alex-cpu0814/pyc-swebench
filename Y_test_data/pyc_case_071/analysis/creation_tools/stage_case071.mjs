import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
const work='E:/CLB_Swe-bench/_work/pyc_batch',p=work+'/case071_spec.json',s=JSON.parse(fs.readFileSync(p,'utf8'));
const parsed={};
for(const [label,exit] of [['base',1],['gold',0]]){
 const dir=work+'/case071-probe-'+label,a=JSON.parse(fs.readFileSync(dir+'/summary.json','utf8')),log=fs.readFileSync(dir+'/stdout.raw.log','utf8');
 if(a.exitCode!==exit||a.error)throw new Error('Unverified '+label);
 parsed[label]=Object.fromEntries([...log.matchAll(/^(tests\/.+?)\s+(PASSED|FAILED|ERROR|SKIPPED)(?:\s+\[.*\])?$/gm)].map(x=>[x[1],x[2]]));
 if(Object.keys(parsed[label]).length!==8||s.probeNodes.some(n=>!(n in parsed[label])))throw new Error('Incomplete or mismatching parameter IDs');
}
s.failToPass=s.probeNodes.filter(n=>parsed.base[n]==='FAILED'&&parsed.gold[n]==='PASSED');
s.passToPass=s.probeNodes.filter(n=>parsed.base[n]==='PASSED'&&parsed.gold[n]==='PASSED');
if(s.failToPass.length!==4||s.passToPass.length!==4)throw new Error('Expected measured four F2P/four P2P nodes');
s.validationStatus='verified_base_gold';
s.verifiedError='Base fails four original parameterized empty-container assertions: {} and [] expand to opening/closing delimiters separated by two newlines, and nested empty containers gain the same extra newline/indentation. The original nonempty four-space parameter and three unchanged encoding/decoding regressions pass. Gold passes all eight official nodes and both equality assertions, including stdlib json.dumps equivalence, for all five parameter inputs. No skip, missing node, native crash or instrumentation observed.';
s.targetSummary='Base: 4 official empty-container parameter targets fail and 4 regressions pass. Gold: all 8 official nodes pass.';
s.verifiedTest=[...s.failToPass,...s.passToPass].join(' and ');
s.testScope='Exact upstream test_encode_indent inputs cover a nonempty object, {}, [], an object containing an empty object, and a list containing an empty list, at indent=4. Both original-format and stdlib-json equality assertions are retained. Four empty/nested inputs are measured FAIL_TO_PASS; the nonempty input and three unchanged dict/list encoding and Unicode decoding tests are PASS_TO_PASS. Real pytest parameter IDs containing spaces and literal escapes are kept exactly; the anchored result parser accepts spaces without decoding or normalizing IDs. No float-representation claim is made.';
s.passingRegressionDescription='The retained nonempty parameter and three unchanged neighboring encoding/decoding functions pass on Base and Gold. The complete upstream parameterized test patch, including the new stdlib-json assertion, is applied to both products.';
const git=args=>{const r=spawnSync('git',['-C',s.sourceRepo,...args],{encoding:'utf8'});if(r.status!==0&&r.status!==1)throw new Error(r.stderr);return r;};
function control(file,transform){const before=git(['show',s.baseCommit+':'+file]).stdout,after=transform(before);if(before===after)throw new Error('Unchanged control');const a=work+'/case071-control-before.txt',b=work+'/case071-control-after.txt';fs.writeFileSync(a,before);fs.writeFileSync(b,after);return git(['diff','--no-index','--',a,b]).stdout.replace(/^diff --git .*$/m,'diff --git a/'+file+' b/'+file).replace(/^--- .*$/m,'--- a/'+file).replace(/^\+\+\+ .*$/m,'+++ b/'+file);}
s.negativePatch=control('README.rst',x=>x.replace('UltraJSON\n=========\n','UltraJSON\n=========\n\nThe negative control leaves empty-container newline and indentation logic unchanged.\n'));
s.tamperPatch=control('tests/test_ujson.py',x=>x.replace('    assert test_input == output\n\n\ndef test_decode_from_unicode():','    assert test_input != output\n\n\ndef test_decode_from_unicode():'));
fs.writeFileSync(p,JSON.stringify(s,null,2)+'\n');
fs.appendFileSync(work+'/case071_progress.md','\n'+new Date().toISOString()+' Base4 empty/nested failures and4passes, Gold8passes. Exact8 parameter/functionIDs measured and matched raw status lines. FixedBase/ancestor4.0.1/SCM4.0.2.dev3; formal controls pending.\n');
console.log(s.targetSummary);
