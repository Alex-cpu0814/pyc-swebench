import datetime,json,pathlib,sys,urllib.request,urllib.error
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');n=sys.argv[1];s=json.loads((w/f'case{n}_spec.json').read_text(encoding='utf-8'));base='https://api.github.com/repos/'+s['repo'];fix=s['fixCommit']
for name,url in [('upstream_commit_api.json',base+'/commits/'+fix),('issue_api.json',base+'/issues/'+s['issueId']),('upstream_associated_prs.json',base+'/commits/'+fix+'/pulls')]:
    target=w/('case'+n+'_'+name)
    if target.exists():print(target.name,'already captured');continue
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'Accept':'application/vnd.github+json','User-Agent':'public-source-benchmark-verification'}),timeout=40)as response:raw=response.read()
    except (urllib.error.URLError,TimeoutError)as error:
        target.with_suffix(target.suffix+'.unavailable.json').write_bytes((json.dumps({'url':url,'error':str(error),'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n').encode());print(target.name,'unavailable');continue
    assert isinstance(json.loads(raw),(dict,list));target.write_bytes(raw);print(target.name,len(raw))
