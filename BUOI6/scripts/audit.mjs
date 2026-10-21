import {spawnSync} from 'node:child_process';
import {readFileSync,mkdirSync,writeFileSync} from 'node:fs';
const result=process.platform==='win32'
  ?spawnSync(process.env.ComSpec||'cmd.exe',['/d','/s','/c','npm.cmd audit --json'],{encoding:'utf8'})
  :spawnSync('npm',['audit','--json'],{encoding:'utf8'});
if(result.error)throw result.error;
const report=JSON.parse(result.stdout.replace(/^\uFEFF/,''));
if(report.error || !report.metadata)throw new Error('Audit failed to retrieve vulnerability data');
const exceptions=JSON.parse(readFileSync('security-exceptions.json','utf8'));
const lock=JSON.parse(readFileSync('package-lock.json','utf8'));
const rejected=[],accepted=[],seen=new Set();
for(const vulnerability of Object.values(report.vulnerabilities||{})) {
  for(const advisory of vulnerability.via) {
    if(typeof advisory==='string'||!['high','critical'].includes(advisory.severity))continue;
    if(seen.has(advisory.url))continue;
    seen.add(advisory.url);
    const id=advisory.url.split('/').pop(), exception=exceptions[id];
    const versions=vulnerability.nodes.map(node=>lock.packages[node]?.version);
    if(exception && exception.package===advisory.name && versions.every(version=>version===exception.version) && new Date(exception.expires+'T00:00:00Z')>new Date())accepted.push({id,package:advisory.name,...exception});
    else rejected.push({id,package:advisory.name,severity:advisory.severity});
  }
}
mkdirSync('reports',{recursive:true});
writeFileSync('reports/audit-after.json',JSON.stringify(report,null,2));
writeFileSync('reports/audit-policy.json',JSON.stringify({time:new Date().toISOString(),accepted,rejected},null,2));
console.log('npm audit totals:',report.metadata.vulnerabilities);
for(const item of accepted)console.log(`EXCEPTION ${item.id}: ${item.package}@${item.version}, expires ${item.expires}`);
for(const item of rejected)console.log(`BLOCK ${item.id}: ${item.package} ${item.severity}`);
console.log(`Audit policy: ${rejected.length} unaccepted high/critical advisory(s)`);
if(rejected.length)process.exitCode=1;
