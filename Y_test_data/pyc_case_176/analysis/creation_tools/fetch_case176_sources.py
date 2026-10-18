"""Preserve public upstream issue, commit and associated-PR metadata."""
import datetime,json,urllib.request,urllib.error
from pathlib import Path
w=Path('E:/CLB_Swe-bench/_work/pyc_batch')
base='https://api.github.com/repos/bcdev/jpy'
fix='81bfc112257504a3ab2cc3de3ae38ca6fa4bbf04'
for name,url in [('upstream_commit_api.json',base+'/commits/'+fix),('issue52_api.json',base+'/issues/52'),('upstream_associated_prs.json',base+'/commits/'+fix+'/pulls')]:
    target=w/('case176_'+name)
    if target.exists():
        print(target.name,'already captured');continue
    req=urllib.request.Request(url,headers={'Accept':'application/vnd.github+json','User-Agent':'public-source-benchmark-verification'})
    try:
        with urllib.request.urlopen(req,timeout=40)as response:raw=response.read()
    except (urllib.error.URLError,TimeoutError)as error:
        evidence={'url':url,'error':str(error),'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
        target.with_suffix(target.suffix+'.unavailable.json').write_bytes((json.dumps(evidence,indent=2)+'\n').encode())
        print(target.name,'unavailable');continue
    obj=json.loads(raw);assert isinstance(obj,(dict,list));target.write_bytes(raw);print(target.name,len(raw))
