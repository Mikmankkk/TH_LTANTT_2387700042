import {readdirSync,statSync,readFileSync,mkdirSync,writeFileSync} from 'node:fs';
import {join,relative} from 'node:path';
import {createHash} from 'node:crypto';
const files={};
function walk(dir){for(const name of readdirSync(dir).sort()){const path=join(dir,name);if(statSync(path).isDirectory())walk(path);else files[relative('build',path).replaceAll('\\','/')]=createHash('sha256').update(readFileSync(path)).digest('hex');}}
walk('build');
mkdirSync('reports',{recursive:true});
writeFileSync('reports/build-sha256.json',JSON.stringify({algorithm:'SHA-256',files},null,2));
console.log(`Artifact: ${Object.keys(files).length} files hashed with SHA-256`);
