from pathlib import Path
import json
w=Path('E:/CLB_Swe-bench/_work/pyc_batch');prev=Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_082/analysis/creation_tools')
for n in ['refresh_case082.mjs','verify_committed_case082.mjs','audit_publication082.mjs','record_publication082.mjs','cleanup_case082.ps1','verify_case082.py']:
    text=(prev/n).read_text(encoding='utf-8').replace('case082','case086').replace('case_082','case_086').replace('case-082','case-086').replace('publication082','publication086')
    if n.startswith('refresh_'):
        text=text.replace("/082.*\\.(mjs|py|ps1)$/.test(n)","n.includes(s.caseNumber)&&/\\.(mjs|py|ps1)$/.test(n)")
    if n.startswith('audit_'):
        text=text.replace('pyc_case_081/verification','pyc_case_082/verification')
    if n.startswith('record_') or n.startswith('cleanup_'):
        text=text.replace('9b466d593d9252da3ccb18d5270b5e8b1dcc456daa31e67273e94d2d48c9256a','11e605344ed4675be7b010289e782843d09aa9efc3fae6d819d905c65ab7a0f3')
    if n.startswith('cleanup_'):
        text=text.replace(" 'case086-image-context'", " 'case083-duplicate'='analysis/prior_candidate_reviews/case083'\n 'case083_progress.md'='analysis/prior_candidate_reviews/case083_authority_progress.md'\n 'review_case083_duplicate.mjs'='analysis/prior_candidate_reviews/case083/review_case083_duplicate.mjs'\n 'case086_upstream_associated_prs.json'='analysis/source_material/upstream_associated_prs.json'\n 'case086_upstream_pr_commits.json'='analysis/source_material/upstream_pr_commits.json'\n 'case086-image-context'")
        text=text.replace("$_.Name -match '082'", "$_.Name -match '086'")
        text=text.replace("$_.Name -match '086' -and", "($_.Name -match '086' -or $_.Name -in @('case083-duplicate','case083_progress.md','review_case083_duplicate.mjs')) -and")
        text=text.replace("'082';status", "'086';status").replace("-match '082.*", "-match '086.*").replace('pygame082-','pygame086-')
    if n.startswith('verify_case'):
        text=text.replace("['src_c/event.c']","['src_c/draw.c']").replace("['test/event_test.py']","['test/draw_test.py']").replace("test/event_test.py::","test/draw_test.py::").replace("v['event_extension']","v['draw_extension']")
        text=text.replace('2019,2,8','2018,8,30').replace('2019,2,11','2018,9,3').replace('2019-02-08T01:34:02Z','2018-08-30T15:02:44Z').replace('2019-02-11T18:21:35Z','2018-09-03T16:22:00Z')
        text=text.replace("api['merge_commit_sha']==s['fixCommit']", "api['merge_commit_sha']==s['provenance']['api_merge_sha'] and s['fixCommit'] in [c['sha'] for c in json.loads(read(r/'analysis/source_material/upstream_pr_commits.json'))]")
        text=text.replace("s['provenance']['source_commit_utc_timestamp']=='2018-09-03T16:22:00Z'", "s['provenance']['source_commit_utc_timestamp']=='2018-08-30T16:17:53Z'")
        text += "\nprior=r/'analysis/prior_candidate_reviews/case083'\nfor line in read(prior/'SHA256SUMS.txt').splitlines():\n    expected,name=line.split('  ',1);assert hashlib.sha256((prior/name).read_bytes()).hexdigest()==expected\nreview=json.loads(read(prior/'duplicate_review.json'));assert review['is_second_parent_of_case081_fix'] and all(v['exact_bytes_equal_to_case081'] for v in review['comparisons'].values())\n"
    (w/n.replace('082','086')).write_text(text,encoding='utf-8',newline='\n')
