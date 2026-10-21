import {readFileSync, readdirSync, statSync, mkdirSync, writeFileSync} from 'node:fs';
import {resolve, relative, extname} from 'node:path';
import {fileURLToPath} from 'node:url';

export function inspect(text, file) {
  const findings = [];
  if (/\b(?:eval|Function)\s*\(/.test(text)) findings.push('dynamic-evaluation');
  if (/-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----/.test(text)) findings.push('private-key');
  if (/(?:gh[pousr]_[A-Za-z0-9]{30,}|AKIA[A-Z0-9]{16}|glpat-[A-Za-z0-9_-]{20,})/.test(text)) findings.push('credential');
  if (/(?:password|secret|api_key)\s*[:=]\s*['"][^'"\s]{8,}['"]/i.test(text)) findings.push('hardcoded-secret');
  if (file.endsWith('Dockerfile') && !/^USER\s+(?!root\b|0\b)\S+/mi.test(text)) findings.push('container-root');
  return findings.map(rule => ({file, rule}));
}
export function scan(root) {
  const findings = [];
  const walk = dir => {
    for (const name of readdirSync(dir)) {
      if (['node_modules','.git','.docusaurus','build','public','reports','evidence','.capture-temp'].includes(name)) continue;
      const path = resolve(dir,name);
      if (statSync(path).isDirectory()) walk(path);
      else if (['.js','.jsx','.mjs','.json','.yml','.yaml','.tf'].includes(extname(path)) || name === 'Dockerfile') {
        if (relative(root,path).replaceAll('\\','/') === 'tests/security.test.mjs') continue;
        findings.push(...inspect(readFileSync(path,'utf8'),relative(root,path)));
      }
    }
  };
  walk(root);
  return findings;
}
if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const findings = scan(process.cwd());
  mkdirSync('reports',{recursive:true});
  writeFileSync('reports/security.json',JSON.stringify({scanner:'supplemental-source-policy',time:new Date().toISOString(),findings},null,2));
  console.log(`Supplemental source policy: ${findings.length} finding(s)`);
  for (const finding of findings) console.log(`${finding.file}: ${finding.rule}`);
  if (findings.length) process.exitCode = 1;
}
