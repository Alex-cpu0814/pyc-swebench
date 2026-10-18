"""Capture public upstream API responses without credentials or host inputs."""
import datetime,json,urllib.request,urllib.error
from pathlib import Path
w=Path('E:/CLB_Swe-bench/_work/pyc_batch')
for name,url in [('case163_upstream_commit_api.json','https://api.github.com/repos/bastibe/lunatic-python/commits/bf894ed520b97645298e4e6eae377b028fc04cab'),('case163_pr5_api.json','https://api.github.com/repos/bastibe/lunatic-python/pulls/5'),('case163_upstream_associated_prs.json','https://api.github.com/repos/bastibe/lunatic-python/commits/bf894ed520b97645298e4e6eae377b028fc04cab/pulls')]:
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
url='https://github.com/bastibe/lunatic-python/pull/5'
with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'public-source-benchmark-verification'}),timeout=45)as response:raw=response.read()
(w/'case163_pr5.raw.html').write_bytes(raw)
print('pr5 public HTML',len(raw))
