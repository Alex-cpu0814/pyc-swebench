import pathlib,re,urllib.request
w=pathlib.Path('E:/CLB_Swe-bench/_work/pyc_batch');url='https://github.com/astrofrog/fast-histogram/pull/52'
with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'public-source-benchmark-verification'}),timeout=45)as response:raw=response.read()
title=re.search(rb'<title>(.*?)</title>',raw,re.S).group(1).decode();assert 'Fix incorrect strides' in title and '#52'in title
(w/'case159_pr52.raw.html').write_bytes(raw);print(title,len(raw))
