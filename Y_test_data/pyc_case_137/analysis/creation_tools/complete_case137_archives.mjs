import fs from 'node:fs';
import {spawnSync} from 'node:child_process';
const w='E:/CLB_Swe-bench/_work/pyc_batch',repo='E:/CLB_Swe-bench/pyc-swebench';
const state=JSON.parse(fs.readFileSync(w+'/batch_state.json','utf8'));
const current=state.candidates.find(c=>c.caseNumber==='137');
if(current.status!=='published_cleaned')throw Error('Complete normal case cleanup first');
const cleanup=JSON.parse(fs.readFileSync(w+'/case137_prior_cleanup.json','utf8'));
const head=spawnSync('git',['-C',repo,'rev-parse','HEAD'],{encoding:'utf8'}).stdout.trim();
if(head!==current.gitCommit||cleanup.publishedCommit!==head||cleanup.status!=='archived_deferred_scratch_cleaned')throw Error('Publication mismatch');
const docker='C:/Users/玉兔/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe';
for(const n of ['128','132','134','137'])if(spawnSync(docker,['image','inspect','pyc-case'+n+'-prototype-base:latest'],{encoding:'utf8'}).status===0)throw Error('Prototype tag still present '+n);
for(const n of cleanup.cases){
 const entry=state.candidates.find(c=>c.caseNumber===n),archive='Y_test_data/pyc_case_137/analysis/prior_candidate_reviews/case'+n;
 Object.assign(entry,{reviewEvidence:archive,archivedIn:'137',archiveCommit:head,reviewScratchCleaned:true,updatedAt:new Date().toISOString()});
 const progress=w+'/case'+n+'_progress.md';
 fs.appendFileSync(progress,'\nImmutable evidence archived at '+archive+' in commit '+head+'. Exact archived scratch bytes were verified before deletion; deferred status is unchanged.\n');
}
fs.writeFileSync(w+'/batch_state.json',JSON.stringify(state,null,2)+'\n');
const next=state.candidates.find(c=>c.status==='pending')?.caseNumber??'none';
const path=w+'/CONTINUATION.md';let text=fs.readFileSync(path,'utf8');
text=text.replace('Cases 081, 082, 086, 088, 090, 091, and094 are published and cleaned.','Cases 081, 082, 086, 088, 090, 091, 094, and137 are published and cleaned.');
text=text.replace(/Case094 is complete:[\s\S]*?(?=\r?\n\r?\n## Reuse)/,'Case137 is complete: exact two-file upstream patch and all four original methods retained. Gold4PASS; native Base phase exit134 after3P2P PASS and target start, with target terminal MISSING, honestly preserved. Formal same-image three controls, actual native/source audit, typed-date two-sheet workbook, complete SHA and actual committed-blob independent review passed. Eight deferred reviews106/107/111/113/114/128/132/134 are immutably archived with their inner manifests. Git remote main and successful Docker publication verified. Exact archived scratch and prototype tags removed; formal/shared images and source caches remain. Next pending candidate'+next+', continue serially from batch_state.json.');
text=text.replace(/Latest published094 commit:[\s\S]*?(?=\r?\n\r?\n## Deferred)/,'Latest published137 commit: `'+head+'`; image digest `'+current.imageDigest+'`. Root independently verified complete file SHA, all8 review archives, and actual committed blobs. Independent registry query: '+current.registryIndependentRecheck+'. Continue'+next+', then remaining pending candidates serially. Preserve recovery state on interruption and report milestones or real blockers to root.');
text=text.replace('## Deferred evidence awaiting next suitable case','## Deferred evidence archived in case137').replace(/- Case(106|107|111|113|114|128|132|134):[^\r\n]*/g,(line,n)=>line+' Immutable location: `pyc-swebench/Y_test_data/pyc_case_137/analysis/prior_candidate_reviews/case'+n+'`; original scratch removed only after exact-byte verification.');
fs.writeFileSync(path,text);
console.log(JSON.stringify({caseNumber:'137',status:current.status,archivedReviews:cleanup.cases,nextPending:next}));
