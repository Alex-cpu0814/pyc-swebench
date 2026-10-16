"""Preserve anonymous public PR/commit bytes, including unavailable responses."""
import datetime,json,urllib.request,urllib.error,sys
from pathlib import Path
w=Path('E:/CLB_Swe-bench/_work/pyc_batch')
for name,url in [('case132_upstream_commit_api.json','https://api.github.com/repos/MSeifert04/iteration_utilities/commits/dc5e033ad648e5373ae1f34d4409380bbd4ab8a1'),('case132_pr198_api.json','https://api.github.com/repos/MSeifert04/iteration_utilities/pulls/198'),('case132_upstream_associated_prs.json','https://api.github.com/repos/MSeifert04/iteration_utilities/commits/dc5e033ad648e5373ae1f34d4409380bbd4ab8a1/pulls'),('case132_pr198.raw.html','https://github.com/MSeifert04/iteration_utilities/pull/198')]:
 if '--html-only'in sys.argv and not name.endswith('.html'):continue
 req=urllib.request.Request(url,headers={'Accept':'text/html'if name.endswith('.html')else'application/vnd.github+json','User-Agent':'public-source-benchmark-verification'})
 try:
  with urllib.request.urlopen(req,timeout=45)as response:raw=response.read()
 except urllib.error.HTTPError as error:
  evidence={'url':url,'status':error.code,'headers':dict(error.headers),'body':error.read().decode('utf-8',errors='replace'),'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  (w/(name+'.unavailable.json')).write_bytes((json.dumps(evidence,indent=2)+'\n').encode())
  print(name,'unavailable',error.code)
  continue
 if not name.endswith('.html'):assert isinstance(json.loads(raw),(dict,list))
 (w/name).write_bytes(raw);print(name,len(raw))
