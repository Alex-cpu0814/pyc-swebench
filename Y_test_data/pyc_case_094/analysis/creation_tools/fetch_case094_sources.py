"""Capture public upstream API responses without credentials or host inputs."""
import datetime,json,urllib.request,urllib.error
from pathlib import Path
w=Path('E:/CLB_Swe-bench/_work/pyc_batch')
for name,url in [('case094_upstream_commit_api.json','https://api.github.com/repos/pygame/pygame/commits/c7ec15285c23ce54f466c9a3482b4d087eb8b0ff'),('case094_issue93_api.json','https://api.github.com/repos/pygame/pygame/issues/93'),('case094_upstream_associated_prs.json','https://api.github.com/repos/pygame/pygame/commits/c7ec15285c23ce54f466c9a3482b4d087eb8b0ff/pulls')]:
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
url='https://github.com/pygame/pygame/issues/93'
with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'public-source-benchmark-verification'}),timeout=45)as response:raw=response.read()
(w/'case094_issue93.raw.html').write_bytes(raw)
print('issue93 public HTML',len(raw))
