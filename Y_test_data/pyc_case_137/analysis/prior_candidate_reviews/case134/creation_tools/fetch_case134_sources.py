"""Preserve anonymous public PR/commit bytes, including unavailable responses."""
import datetime,json,urllib.request,urllib.error,sys
from pathlib import Path
w=Path('E:/CLB_Swe-bench/_work/pyc_batch')
for name,url in [('case134_upstream_commit_api.json','https://api.github.com/repos/MSeifert04/iteration_utilities/commits/1361a3a3e1c0d75dd4ee2ad2609d2f795bcdfc6f'),('case134_pr192_api.json','https://api.github.com/repos/MSeifert04/iteration_utilities/pulls/192'),('case134_upstream_associated_prs.json','https://api.github.com/repos/MSeifert04/iteration_utilities/commits/1361a3a3e1c0d75dd4ee2ad2609d2f795bcdfc6f/pulls'),('case134_pr192.raw.html','https://github.com/MSeifert04/iteration_utilities/pull/192')]:
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
