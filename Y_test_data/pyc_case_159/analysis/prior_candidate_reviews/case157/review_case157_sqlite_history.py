import datetime,json,pathlib,urllib.request,urllib.error
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');out=w/'case157-sqlite-history-review';out.mkdir()
sources=[('sqlite321-prepare.c','https://raw.githubusercontent.com/sqlite/sqlite/version-3.2.1/src/prepare.c'),('sqlite321-header.h.in','https://raw.githubusercontent.com/sqlite/sqlite/version-3.2.1/src/sqlite.h.in'),('sqlite-prepare-current.raw.html','https://sqlite.org/c3ref/prepare.html')]
records=[]
for name,url in sources:
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'public-source-benchmark-verification'}),timeout=45)as response:raw=response.read();status=response.status
  (out/name).write_bytes(raw);records.append({'url':url,'file':name,'status':status,'bytes':len(raw)})
 except (urllib.error.HTTPError,urllib.error.URLError,TimeoutError)as exc:
  records.append({'url':url,'error':str(exc),'status':getattr(exc,'code',None)})
(out/'capture.json').write_bytes((json.dumps({'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'requests':records},indent=2)+'\n').encode());print(json.dumps(records))
