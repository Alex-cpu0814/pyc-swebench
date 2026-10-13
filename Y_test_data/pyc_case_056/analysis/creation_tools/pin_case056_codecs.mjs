import fs from 'node:fs';const work='E:/CLB_Swe-bench/_work/pyc_batch',p=work+'/case056_spec.json',s=JSON.parse(fs.readFileSync(p,'utf8')),audit=JSON.parse(fs.readFileSync(work+'/case056-dependency-audit/summary.json','utf8'));
if(audit.exitCode!==0||audit.error||!audit.codec_audit||!Object.values(audit.codec_audit.codec_support).every(Boolean))throw new Error('Required codec audit failed');
const opj=audit.native_package_versions['libopenjp2-7-dev'],tiff=audit.native_package_versions['libtiff-dev'];if(!opj||!tiff)throw new Error('Explicit codec package versions missing');
let dockerfile=fs.readFileSync(s.dockerfileSource,'utf8');dockerfile=dockerfile.replace('libopenjp2-7-dev libtiff-dev',`libopenjp2-7-dev=${opj} libtiff-dev=${tiff}`);fs.writeFileSync(s.dockerfileSource,dockerfile);
s.provenance.native_package_versions=audit.native_package_versions;s.provenance.required_codec_support=audit.codec_audit.codec_support;s.provenance.required_codec_versions=audit.codec_audit.codec_versions;
s.nativeRequirement=Object.entries(audit.native_package_versions).map(([name,version])=>`${name}=${version}`).join('; ');fs.writeFileSync(p,JSON.stringify(s,null,2)+'\n');
console.log('056 OpenJPEG/TIFF explicitly version-pinned from successful required-codec audit.');
