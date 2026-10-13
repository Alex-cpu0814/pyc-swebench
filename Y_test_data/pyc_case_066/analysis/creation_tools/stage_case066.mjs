import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
const work='E:/CLB_Swe-bench/_work/pyc_batch',p=work+'/case066_spec.json',s=JSON.parse(fs.readFileSync(p,'utf8'));
for(const [label,exit] of [['base',1],['gold',0]]){
 const dir=work+'/case066-probe-'+label+'-v3',a=JSON.parse(fs.readFileSync(dir+'/summary.json','utf8')),log=fs.readFileSync(dir+'/stdout.raw.log','utf8');
 if(a.exitCode!==exit||a.error)throw new Error('Unverified '+label);
 for(const node of s.probeNodes){const expected=label==='base'&&node.includes('TestDefaultFontLeak')?'FAILED':'PASSED';if(!log.split('\n').includes(node+' '+expected))throw new Error(node+' '+expected);}
}
s.failToPass=['Tests/test_font_leaks.py::TestDefaultFontLeak::test_leak'];
s.passToPass=s.probeNodes.filter(x=>!s.failToPass.includes(x));
s.probeSuffixes={base:'-v3',gold:'-v3'};
s.validationStatus='verified_base_gold';
s.verifiedError='Base original unittest DefaultFont leak fails: AssertionError 1164 not less than 1024, memory usage limit exceeded in iteration 46. Gold passes this target and all three regressions. TrueType leak passes on both Base and Gold at its original 4096 KiB / 10 iteration limit, so it is PASS_TO_PASS in this environment. Normal default-font and PNG sanity tests pass on both.';
s.targetSummary='Base: 1 font leak target fails and 3 regressions pass. Gold: all 4 official nodes pass without skips.';
s.verifiedTest=[...s.failToPass,...s.passToPass].join(' and ');
s.testScope='Original official unittest cases execute once each in fresh subprocesses. DefaultFont uses 100 iterations and 1024 KiB, TrueType uses 10 iterations and 4096 KiB. Thresholds, loops and test bodies are unchanged. TrueType Base pass does not independently verify the FreeType leak repair in this allocator/dependency environment. The complete two-file upstream C product patch is retained. Initial pytest PNG cleanup incompatibility and DefaultFont assertion, plus the sandbox Docker permission error, remain authoring evidence.';
s.provenance.runner_scope=s.testExecution;
s.provenance.discriminating_target='TestDefaultFontLeak.test_leak';
s.provenance.truetype_limitation='TrueType original official RSS test passes Base and Gold in this environment and is PASS_TO_PASS; no independent FAIL_TO_PASS claim for _imagingft.c.';
const git=args=>{const r=spawnSync('git',['-C',s.sourceRepo,...args],{encoding:'utf8'});if(r.status!==0&&r.status!==1)throw new Error(r.stderr);return r;};
function control(file,transform){const before=git(['show',s.baseCommit+':'+file]).stdout,after=transform(before);if(before===after)throw new Error('Unchanged control');const a=work+'/case066-control-before.txt',b=work+'/case066-control-after.txt';fs.writeFileSync(a,before);fs.writeFileSync(b,after);return git(['diff','--no-index','--',a,b]).stdout.replace(/^diff --git .*$/m,'diff --git a/'+file+' b/'+file).replace(/^--- .*$/m,'--- a/'+file).replace(/^\+\+\+ .*$/m,'+++ b/'+file);}
s.negativePatch=control('README.rst',x=>x.replace('Pillow\n======\n','Pillow\n======\n\nThe negative control leaves native font resources unchanged.\n'));
s.tamperPatch=control('Tests/test_file_png.py',x=>x.replace('from helper import unittest, PillowTestCase, hopper','from helper import unittest, PillowTestCase'));
fs.writeFileSync(p,JSON.stringify(s,null,2)+'\n');
fs.appendFileSync(work+'/case066_progress.md','\n'+new Date().toISOString()+' unittest Base-v3: DefaultFont 1164 >=1024 KiB at iteration46, three passes including TrueType. Gold-v3 all four passed. One F2P/three P2P, thresholds unchanged. Original pytest and permission-denied evidence retained. Formal build/controls pending.\n');
console.log(s.targetSummary);
