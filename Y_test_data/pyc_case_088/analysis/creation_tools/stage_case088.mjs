import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
const w='E:/CLB_Swe-bench/_work/pyc_batch',p=w+'/case088_spec.json',s=JSON.parse(fs.readFileSync(p,'utf8'));
const check=(ok,msg)=>{if(!ok)throw Error(msg);};
const collected=fs.readFileSync(w+'/case088-probe-collect-v3/stdout.raw.log','utf8').trim().split('\n');
check(JSON.stringify(collected)===JSON.stringify(s.probeNodes),'Collection mismatch');
for(const[label,exit]of[['base',1],['gold',0]]){
 const a=JSON.parse(fs.readFileSync(w+'/case088-probe-'+label+'-v3/summary.json','utf8')),log=fs.readFileSync(w+'/case088-probe-'+label+'-v3/stdout.raw.log','utf8');
 check(a.exitCode===exit&&!a.error,'Unverified '+label);
 const statuses=Object.fromEntries([...log.matchAll(/^(test\/\S+) (PASSED|FAILED|ERROR)$/gm)].map(m=>[m[1],m[2]]));
 check(Object.keys(statuses).length===4,'Missing statuses');
 for(const node of collected)check(statuses[node]===(label==='base'&&s.failToPass.includes(node)?'FAILED':'PASSED'),'Unexpected '+label+' '+node);
 const records=log.split('\n').filter(l=>l.startsWith('OFFICIAL_PROCESS_RECORD ')).map(l=>JSON.parse(l.slice(24)));
 check(records.length===4,'Missing process records');
 for(const r of records){
  const child=Buffer.from(r.stdout_base64,'base64').toString('utf8');
  check(child.includes('OFFICIAL_TEST_START '+r.node),'Test not started');
  if(label==='base'&&s.failToPass.includes(r.node)){
   check(r.returncode===-6,'Expected observed SIGABRT');
   check(Buffer.from(r.stderr_base64,'base64').toString('utf8').includes('Segmentation Fault'),'Missing pygame parachute evidence');
  }else check(r.returncode===0&&child.includes('"testsRun": 1')&&child.includes('"status": "PASSED"'),'Missing true official result');
 }
}
s.probeSuffix='-v3';s.validationStatus='verified_base_gold';s.validationType='official_bundled_unittest';s.evidenceType='source_row_upstream_issue_and_verified_bundled_unittest_trace';s.workbookDateFields=true;
s.verifiedError='Base completes test_copy, test_get_bytesize and test_get_rect. In the unchanged complete test_get_bounding_rect, the official added 4 by 1, 8-bit filled Surface call triggers pygame parachute Segmentation Fault at test/surface_test.py:173 and ends the child with return code -6 (SIGABRT). The wrapper records native failure and exits 1. Gold completes all four original methods with testsRun=1, wasSuccessful and normal child exits.';
s.targetSummary='Base: one official bounding-rectangle method terminates with SIGABRT after pygame reports Segmentation Fault; three regressions pass. Gold: all four official methods pass.';
s.verifiedTest=[...s.failToPass,...s.passToPass].join(' and ');
s.testScope='The full official test_get_bounding_rect method first retains existing alpha/color-key rectangle assertions, then initializes the display, creates the exact 4 by 1, 8-bit Surface, fills white and calls get_bounding_rect within the original try/finally pygame.quit. This added call asserts completion, with no new returned-rectangle assertion. Unchanged test_copy, test_get_bytesize and test_get_rect provide three regressions. Product patch changes four native bounding scans to handle 1/2/3/4 bytes per pixel with endian-aware 24-bit assembly. Only this original 8-bit failure and the complete selected methods are measured; other bit depths, endian systems and scan branches are not separately claimed.';
s.passingRegressionDescription='Three unchanged complete official SurfaceTypeTest methods pass on Base and Gold.';
s.sourceTraceNotes='Source case87 names surf_get_bounding_rect through test_get_bounding_rect; this complete original method is actually observed failing in the source first parent and passing with the full exact product patch. Issue180 opened2013-10-21; source fix committed2013-10-28. Associated PR lookup is empty and no merge date exists. Issue migration closure2017-03-26 is not a merge date.';
const a=JSON.parse(fs.readFileSync(w+'/case088-runtime-audit-v2/summary.json','utf8'));check(a.exitCode===0,'Prototype audit failed');s.provenance.native_package_versions=a.native_package_versions;s.provenance.source_trace_scope=s.sourceTraceNotes;s.provenance.verified_scope=s.testScope;
const git=args=>{const r=spawnSync('git',['-C',s.sourceRepo,...args],{encoding:'utf8',maxBuffer:8*1024*1024});check(r.status===0||r.status===1,r.stderr);return r.stdout;};
function control(file,fn){const before=git(['show',s.baseCommit+':'+file]),after=fn(before);check(before!==after,'Unchanged control');const x=w+'/case088-control-before.txt',y=w+'/case088-control-after.txt';fs.writeFileSync(x,before);fs.writeFileSync(y,after);return git(['diff','--no-index','--',x,y]).replace(/^diff --git .*$/m,'diff --git a/'+file+' b/'+file).replace(/^--- .*$/m,'--- a/'+file).replace(/^\+\+\+ .*$/m,'+++ b/'+file);}
s.negativePatch=control('readme.rst',x=>x+'\nThis evaluator control leaves Surface bounding scans unchanged.\n');
s.tamperPatch=control('test/surface_test.py',x=>x.replace('        self.assertEqual(bound_rect.height, 31)','        self.assertEqual(bound_rect.height, 30)'));
check(s.tamperPatch.includes('-        self.assertEqual(bound_rect.height, 31)'),'Missing protected context');
fs.writeFileSync(w+'/case088_collected_nodes.json',JSON.stringify({nodes:collected,count:4,source:'Actual official bundled unittest loader countTestCases=1 for each unchanged complete method; exact official test patch'},null,2)+'\n');
fs.writeFileSync(p,JSON.stringify(s,null,2)+'\n');console.log(s.targetSummary);
