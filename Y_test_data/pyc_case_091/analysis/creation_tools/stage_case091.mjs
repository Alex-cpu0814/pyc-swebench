import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
const w='E:/CLB_Swe-bench/_work/pyc_batch',p=w+'/case091_spec.json',s=JSON.parse(fs.readFileSync(p,'utf8'));
const check=(v,m)=>{if(!v)throw Error(m);};
const collected=fs.readFileSync(w+'/case091-probe-collect/stdout.raw.log','utf8').trim().split('\n');
check(JSON.stringify(collected)===JSON.stringify(s.probeNodes),'Collection mismatch');
for(const [label,exit]of [['base',1],['gold',0]]){
 const a=JSON.parse(fs.readFileSync(w+'/case091-probe-'+label+'/summary.json','utf8')),log=fs.readFileSync(w+'/case091-probe-'+label+'/stdout.raw.log','utf8');
 check(a.exitCode===exit&&!a.error,'Unverified '+label);
 const statuses=Object.fromEntries([...log.matchAll(/^(test\/\S+) (PASSED|FAILED|ERROR)$/gm)].map(x=>[x[1],x[2]]));check(Object.keys(statuses).length===4,'Missing node');
 for(const n of collected)check(statuses[n]===(label==='base'&&s.failToPass.includes(n)?'FAILED':'PASSED'),'Unexpected status');
 for(const r of log.split('\n').filter(l=>l.startsWith('OFFICIAL_PROCESS_RECORD ')).map(l=>JSON.parse(l.slice(24)))){
  const child=Buffer.from(r.stdout_base64,'base64').toString('utf8'),result=child.split('\n').filter(l=>l.startsWith('OFFICIAL_RESULT ')).map(l=>JSON.parse(l.slice(16)));
  check(result.length===1&&result[0].testsRun===1&&result[0].errors===0,'Incomplete actual method');check(r.returncode===(label==='base'&&s.failToPass.includes(r.node)?1:0),'Unexpected child exit');
 }
}
s.validationStatus='verified_base_gold';
s.verifiedError='Base complete official test_issue_243 stops at its first assertion in test/freetype_test.py:1351: self.assertTrue(r1.width > 1), AssertionError: None, child exit1, testsRun1/failures1/errors0. Its later two-space assertions are not reached on Base. Gold completes the original one-space and two-space boundary assertions. The three complete get_rect, mono-render and issue242 regression methods pass both; issue242 includes the exact upstream two-space to one-space underline-input change.';
s.targetSummary='Base: complete official issue243 fails its first one-space width assertion; three regressions pass. Gold: all four complete official methods pass, including one-space/two-space widths and the upstream-modified issue242.';
s.verifiedTest=[...s.failToPass,...s.passToPass].join(' and ');
s.testScope='Complete original test_issue_243 uses self._TEST_FONTS[fixed] at size64, calls get_rect for one space and asserts width>1, then calls get_rect for two spaces and asserts twice the one-space width. Base stops at the first width assertion; Gold completes both assertions. Three complete official regression methods cover get_rect geometry, monochrome rendering, and all four issue242 style comparisons. The complete upstream test patch modifies issue242 underline input from two spaces to one. Official test bodies/inputs/assertions and Base font fixtures are preserved exactly as upstream. No full freetype suite, independent Base failure of the later two-space assertion, crash, or other fonts/platforms is claimed.';
s.passingRegressionDescription='Three complete official get_rect, mono-render and issue242 methods pass both Base and Gold; issue242 includes the exact upstream one-space underline-input modification.';
s.provenance.verified_scope=s.testScope;s.provenance.source_trace_scope=s.sourceTraceNotes;
const a=JSON.parse(fs.readFileSync(w+'/case091-runtime-audit/summary.json','utf8'));check(a.exitCode===0,'Native audit failed');s.provenance.native_package_versions=a.native_package_versions;
const git=args=>{const r=spawnSync('git',['-C',s.sourceRepo,...args],{encoding:'utf8'});check(r.status===0||r.status===1,r.stderr);return r.stdout;};
function control(file,fn){const before=git(['show',s.baseCommit+':'+file]),after=fn(before);check(before!==after,'Unchanged');const a=w+'/case091-control-before.txt',b=w+'/case091-control-after.txt';fs.writeFileSync(a,before);fs.writeFileSync(b,after);return git(['diff','--no-index','--',a,b]).replace(/^diff --git .*$/m,'diff --git a/'+file+' b/'+file).replace(/^--- .*$/m,'--- a/'+file).replace(/^\+\+\+ .*$/m,'+++ b/'+file);}
s.negativePatch=control('readme.rst',x=>x+'\nThis evaluator control leaves freetype trailing-space bounds unchanged.\n');
s.tamperPatch=control('test/freetype_test.py',x=>x.replace("            rect = font.get_rect('  ', size=64)","            rect = font.get_rect('X', size=64)  # Protected-test conflict control"));
fs.writeFileSync(w+'/case091_collected_nodes.json',JSON.stringify({nodes:collected,count:4,source:'Actual bundled official unittest TestLoader per-method suite count=1'},null,2)+'\n');
fs.writeFileSync(p,JSON.stringify(s,null,2)+'\n');console.log(s.targetSummary);
