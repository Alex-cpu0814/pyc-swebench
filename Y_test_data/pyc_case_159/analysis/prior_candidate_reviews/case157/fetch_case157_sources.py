"""Capture actual public commit provenance without inventing a modern issue identity."""
import json,urllib.request,pathlib
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');base='https://api.github.com/repos/ghaering/pysqlite/commits/ae4c5454849f3e0d08c35ebfface95d297340a14'
for name,url in [('case157_upstream_commit_api.json',base),('case157_upstream_associated_prs.json',base+'/pulls')]:
 with urllib.request.urlopen(urllib.request.Request(url,headers={'Accept':'application/vnd.github+json','User-Agent':'public-source-benchmark-verification'}),timeout=45)as response:raw=response.read()
 assert isinstance(json.loads(raw),(dict,list));(w/name).write_bytes(raw);print(name,len(raw))
url='https://github.com/ghaering/pysqlite/commit/ae4c5454849f3e0d08c35ebfface95d297340a14'
with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'public-source-benchmark-verification'}),timeout=45)as response:raw=response.read()
(w/'case157_commit.raw.html').write_bytes(raw);print('commit HTML',len(raw))
