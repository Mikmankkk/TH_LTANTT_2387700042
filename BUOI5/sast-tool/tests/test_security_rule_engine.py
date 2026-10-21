import json
import pytest
from sast_tool.security_rule_engine import SecurityRuleEngine


def test_default_severity_does_not_mutate():
    issue = dict(rule_id='dangerous-call')
    assert SecurityRuleEngine().evaluate([issue])[0]['severity'] == 'high'
    assert 'severity' not in issue


def test_custom_disable(tmp_path):
    path = tmp_path / 'rules.json'
    path.write_text(json.dumps([dict(id='custom', severity='low', enabled=False)]))
    assert SecurityRuleEngine(path).evaluate([dict(rule_id='custom')]) == []


def test_invalid_rule(tmp_path):
    path = tmp_path / 'rules.json'
    path.write_text('[{"id":"x","severity":"oops"}]')
    with pytest.raises(ValueError):
        SecurityRuleEngine(path)
