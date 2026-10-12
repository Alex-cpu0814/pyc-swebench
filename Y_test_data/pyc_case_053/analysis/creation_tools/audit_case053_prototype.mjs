import fs from 'node:fs';import {spawnSync} from 'node:child_process';
const work='E:/CLB_Swe-bench/_work/pyc_batch',s=JSON.parse(fs.readFileSync(work+'/case053_spec.json','utf8'));
const cmd=`set -euo pipefail; git apply --check /tmp/test.diff; git apply /tmp/test.diff; test "$(git hash-object Tests/images/imagedraw_rectangle_I.png)" = "${s.provenance.binary_test_asset_gold_blob}"; echo BINARY_TEST_ASSET_MATCHES_UPSTREAM; dpkg-query -W gcc libjpeg62-turbo-dev zlib1g-dev libfreetype6-dev libfreetype6; python -c 'import PIL; from PIL import features; print(PIL.__file__); print(features.version("freetype2"))'`;
const image=process.argv.includes('--formal')?s.image:s.prototypeImage;
const args=['run','--rm','--network','none','--mount','type=bind,source='+s.testPatchSource+',target=/tmp/test.diff,readonly','--entrypoint','/bin/bash',image,'-lc',cmd];
const r=spawnSync('C:/Users/玉兔/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe',args,{encoding:'utf8',timeout:120000});
const prefix=process.argv.includes('--formal')?'formal-dependency-and-asset-audit':'dependency-and-asset-audit-v2';
fs.writeFileSync(work+'/case053-prototype-build/'+prefix+'.stdout.raw.log',r.stdout??'');fs.writeFileSync(work+'/case053-prototype-build/'+prefix+'.stderr.raw.log',r.stderr??'');console.log(r.stdout);console.log(r.stderr);process.exitCode=r.status;
