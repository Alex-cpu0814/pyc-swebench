import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
const work='E:/CLB_Swe-bench/_work/pyc_batch',p=work+'/case068_spec.json',s=JSON.parse(fs.readFileSync(p,'utf8'));
for(const [label,exit] of [['base',1],['gold',0]]){
 const dir=work+'/case068-probe-'+label,a=JSON.parse(fs.readFileSync(dir+'/summary.json','utf8')),log=fs.readFileSync(dir+'/stdout.raw.log','utf8');
 if(a.exitCode!==exit||a.error)throw new Error('Unverified '+label);
 for(const node of s.probeNodes){const expected=label==='base'&&s.failToPass.includes(node)?'FAILED':'PASSED';if(!log.split('\n').includes(node+' '+expected))throw new Error(node+' '+expected);}
}
s.pillowVersionAttribute='PILLOW_VERSION';
s.validationStatus='verified_base_gold';
s.verifiedError='Base five official targets fail: RGBA palette roundtrip average pixel difference 162.9834 exceeds the upstream limit of 20; indexed transparency retains incorrect scalar/tuple values and PNG saves raise TypeError; default RGBA quantization raises ValueError: image has wrong mode. Original official tester counters record each failure. Three unchanged conversion/quantization regressions pass. Gold passes all eight nodes without skips or process signals. Product changes are Python-only, no native crash reproduced.';
s.targetSummary='Base: 5 official targets fail and 3 regressions pass. Gold: all 8 official nodes pass without skips.';
s.verifiedTest=[...s.failToPass,...s.passToPass].join(' and ');
s.testScope='Five unchanged upstream functions cover RGBA-to-palette similarity at epsilon 20, indexed P/L/RGB transparency conversion and saving, default RGBA quantization and rejection of unsupported method 0. Three unchanged regressions cover normal default conversion, 8-bit float conversion and 100-color octree quantization. Each function executes once in a fresh process; original tester assertion counters and yield_test callbacks are preserved. An explicit node status and positive assertion count are required for passing, so os._exit(0) skip cannot pass grading. No new assertions, thresholds, image assets or product changes beyond the exact upstream patch are introduced.';
s.sourceTraceNotes=s.sourceTraceNotes.replace('case67','case 67');
s.provenance.source_trace_scope=s.sourceTraceNotes;
s.provenance.merge_identity_limitation='The PR API merge commit fa165c8d70062d1dac943f51d861559b0433cf49 differs from the fixed source commit 6e2075e25d49fa0ffaec5892b64e3dd4cd39a9fd. The source commit API verifies PR574 merge subject, parents and the same UTC merge timestamp. The alternate fa165 object returns HTTP 422, so tree or content equivalence cannot be checked. All patches and tests use source 6e2075 and its verified first parent.';
s.mergeIdentityLimitation=s.provenance.merge_identity_limitation;
s.provenance.runner_scope=s.testExecution;
const git=args=>{const r=spawnSync('git',['-C',s.sourceRepo,...args],{encoding:'utf8'});if(r.status!==0&&r.status!==1)throw new Error(r.stderr);return r;};
function control(file,transform){const before=git(['show',s.baseCommit+':'+file]).stdout,after=transform(before);if(before===after)throw new Error('Unchanged control');const a=work+'/case068-control-before.txt',b=work+'/case068-control-after.txt';fs.writeFileSync(a,before);fs.writeFileSync(b,after);return git(['diff','--no-index','--',a,b]).stdout.replace(/^diff --git .*$/m,'diff --git a/'+file+' b/'+file).replace(/^--- .*$/m,'--- a/'+file).replace(/^\+\+\+ .*$/m,'+++ b/'+file);}
s.negativePatch=control('README.rst',x=>'The negative control leaves indexed transparency and RGBA quantization unchanged.\n\n'+x);
s.tamperPatch=control('Tests/tester.py',x=>x.replace('def warn_error(message, category, **options):','def warn_error(message, category=RuntimeWarning, **options):'));
fs.writeFileSync(p,JSON.stringify(s,null,2)+'\n');
fs.appendFileSync(work+'/case068_progress.md','\n'+new Date().toISOString()+' Base5 target failures/3regressions pass; Gold8 passes. Actual errors: similarity162.9834>20, transparency types/values and PNG TypeError, RGBA quantization ValueError. No crash. Source commitREST6e matches pinned parents/time/PR574 subject, APIalternate mergefa165 unavailableHTTP422; no equivalence claim. Formal controls pending.\n');
console.log(s.targetSummary);
