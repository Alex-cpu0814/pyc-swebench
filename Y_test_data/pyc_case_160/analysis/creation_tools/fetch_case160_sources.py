"""Capture public upstream API responses without credentials or host inputs."""
import datetime,json,urllib.request,urllib.error
from pathlib import Path
w=Path('E:/CLB_Swe-bench/_work/pyc_batch')
for name,url in [('case160_upstream_commit_api.json','https://api.github.com/repos/astrofrog/fast-histogram/commits/e384cdf1fec4ee65a594ca4e91478eb3c98b2d18'),('case160_pr21_api.json','https://api.github.com/repos/astrofrog/fast-histogram/pulls/21'),('case160_upstream_associated_prs.json','https://api.github.com/repos/astrofrog/fast-histogram/commits/e384cdf1fec4ee65a594ca4e91478eb3c98b2d18/pulls')]:
 req=urllib.request.Request(url,headers={'Accept':'application/vnd.github+json','User-Agent':'public-source-benchmark-verification'})
 try:
  with urllib.request.urlopen(req,timeout=45)as response:raw=response.read()
 except urllib.error.HTTPError as error:
  evidence={'url':url,'status':error.code,'headers':dict(error.headers),'body':error.read().decode('utf-8',errors='replace'),'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  (w/(name+'.unavailable.json')).write_bytes((json.dumps(evidence,indent=2)+'\n').encode('utf-8'))
  print(name,'unavailable',error.code)
  continue
 obj=json.loads(raw);assert isinstance(obj,(dict,list));(w/name).write_bytes(raw)
 print(name,len(raw))
url='https://github.com/astrofrog/fast-histogram/pull/21'
with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'public-source-benchmark-verification'}),timeout=45)as response:raw=response.read()
(w/'case160_pr21.raw.html').write_bytes(raw)
print('pr21 public HTML',len(raw))
