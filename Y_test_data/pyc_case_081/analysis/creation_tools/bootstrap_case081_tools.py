"""Prepare reviewable, case-specific finishing tools from the verified workflow."""
from pathlib import Path

w = Path('E:/CLB_Swe-bench/_work/pyc_batch')
previous = Path('E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_077/analysis/creation_tools')

def put(name, content):
    with (w/name).open('w', encoding='utf-8', newline='\n') as stream:
        stream.write(content)

for stem, extension in [('refresh_case','.mjs'), ('verify_committed_case','.mjs'),
                        ('audit_publication','.mjs'), ('record_publication','.mjs')]:
    text = (previous/(stem+'077'+extension)).read_text(encoding='utf-8').replace('077','081')
    text = text.replace('9033751a383ee84641f989c2efc2da75bec96025e77dda11dd9736a992a9a912',
                        '4e5d69e396505fea954f28acb59dc90ef522bafab05dd484c0299e628f938720')
    text = text.replace('case_075/verification/publication', 'case_077/verification/publication')
    text = text.replace("current_user_instruction:'继续下一条'", "current_user_instruction:'继续下一条数据'")
    put(stem+'081'+extension, text)

text=(previous/'verify_case077.py').read_text(encoding='utf-8').replace('077','081')
replacements={
    "['src_c/draw.c']":"['src_c/_freetype.c']",
    "['test/draw_test.py']":"['test/freetype_test.py']",
    'datetime.date(2021,12,18)':'datetime.date(2018,12,30)',
    'datetime.date(2021,12,19)':'datetime.date(2018,12,31)',
    '2021-12-18T16:17:19Z':'2018-12-30T17:11:06Z',
    '2021-12-19T12:15:55Z':'2018-12-31T10:00:19Z',
    '2021-12-19T12:15:54Z':'2018-12-31T10:00:18Z',
    '2.1.1.dev1':'1.9.5.dev0',
    "v['draw_extension']":"v['freetype_extension']",
    "x.startswith('test/')":"x.startswith('test/freetype_test.py::')",
}
for before,after in replacements.items():text=text.replace(before,after)
text=text.replace("assert audits[0]['runtime_audit']==audits[1]['runtime_audit'];raw=", """for a in audits:
    v=a['runtime_audit']; assert v['video_driver']=='x11' and v['freetype_version']==[2,10,4] and v['default_font_height']>0
    assets=v['assets']; assert assets['src_py/freesansbold.ttf']==assets['build/local/pygame/freesansbold.ttf']
    assert assets['src_py/freesansbold.ttf']['sha256']=='bf9251269f11e4b35582a99376096deee3d0c4973a459cbd97b0bebc01f440ad'
    assert len(a['source_git_identity']['font_git_blobs'])==6
assert audits[0]['runtime_audit']==audits[1]['runtime_audit'];raw=""")
put('verify_case081.py',text)
print('Prepared 081 finishing tools, preserving exact runtime and workbook checks.')
