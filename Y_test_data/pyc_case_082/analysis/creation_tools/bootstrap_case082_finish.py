from pathlib import Path
w=Path('E:/CLB_Swe-bench/_work/pyc_batch');prev=Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_081/analysis/creation_tools')
for n in ['audit_publication081.mjs','record_publication081.mjs','verify_committed_case081.mjs']:
    text=(prev/n).read_text(encoding='utf-8').replace('case081','case082').replace('case_081','case_082').replace('publication081','publication082')
    if n.startswith('audit_'):
        text=text.replace('pyc_case_077/verification','pyc_case_081/verification').replace("current_user_instruction:'继续下一条数据'","current_user_instruction:'然后后面你自行制作即可 按顺序 不用问我'")
    if n.startswith('record_'):
        text=text.replace('4e5d69e396505fea954f28acb59dc90ef522bafab05dd484c0299e628f938720','9b466d593d9252da3ccb18d5270b5e8b1dcc456daa31e67273e94d2d48c9256a')
    (w/n.replace('081','082')).write_text(text,encoding='utf-8',newline='\n')
