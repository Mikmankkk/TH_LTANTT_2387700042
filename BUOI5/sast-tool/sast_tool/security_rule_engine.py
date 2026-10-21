import json
from pathlib import Path


class SecurityRuleEngine:
    def __init__(self, rules_file=None):
        path = rules_file or Path(__file__).resolve().parents[1] / 'rules/default_rules.json'
        self.rules = json.loads(Path(path).read_text(encoding='utf-8'))
        ids = [r['id'] for r in self.rules]
        if len(ids) != len(set(ids)) or any(r.get('severity') not in ('high', 'medium', 'low') for r in self.rules):
            raise ValueError('Rules must have unique IDs and valid severities')

    def evaluate(self, *groups):
        rules = {r['id']: r for r in self.rules}
        return [dict(i, severity=rules.get(i['rule_id'], {}).get('severity', 'medium'))
                for group in groups for i in group if rules.get(i['rule_id'], {}).get('enabled', True)]
