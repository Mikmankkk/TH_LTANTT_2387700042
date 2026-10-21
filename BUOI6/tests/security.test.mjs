import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import YAML from 'yaml';
import {inspect} from '../scripts/security-check.mjs';

test('security gate detects dynamic execution',()=>assert.equal(inspect('eval(input)','demo.js')[0].rule,'dynamic-evaluation'));
test('security gate detects a private key',()=>assert.equal(inspect('-----BEGIN PRIVATE KEY-----','key.js')[0].rule,'private-key'));
test('security gate detects an embedded credential',()=>assert.equal(inspect('ghp_'+'a'.repeat(36),'config.js')[0].rule,'credential'));
test('security gate detects hardcoded password',()=>assert.equal(inspect('password = "unsafe-example"','config.js')[0].rule,'hardcoded-secret'));
test('IaC gate rejects root container',()=>assert.equal(inspect('FROM nginx\nUSER root','Dockerfile')[0].rule,'container-root'));
test('IaC gate accepts unprivileged container',()=>assert.deepEqual(inspect('FROM nginx\nUSER 101','Dockerfile'),[]));
test('safe source passes',()=>assert.deepEqual(inspect('const value = JSON.parse(input);','app.js'),[]));
const pipeline=YAML.parse(readFileSync('.gitlab-ci.yml','utf8'));
test('GitLab deploy occurs after mandatory security and build stages',()=>{
  assert.deepEqual(pipeline.stages,['test','security','build','deploy']);
  for(const name of ['security-check','dependency-audit','semgrep','secret-scan']) {
    assert.equal(pipeline[name].stage,'security');
    assert.notEqual(pipeline[name].allow_failure,true);
  }
  assert.equal(pipeline.pages.stage,'deploy');
  assert.deepEqual(pipeline.pages.dependencies,['build-job']);
  assert.equal(pipeline.pages.pages.publish,'public');
  assert.equal(pipeline.pages.rules[0].if,'$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH');
});
test('root GitLab config includes lab pipeline',()=>{
  const root=YAML.parse(readFileSync('../.gitlab-ci.yml','utf8'));
  assert.equal(root.include[0].local,'/BUOI6/.gitlab-ci.yml');
});
test('basic lab preserves four jobs and 20 second test',()=>{
  const basic=YAML.parse(readFileSync('examples/basic.gitlab-ci.yml','utf8'));
  for(const name of ['build-job','test-job1','test-job2','deploy-prod']) assert.ok(basic[name]);
  assert.ok(basic['test-job2'].script.includes('sleep 20'));
});
