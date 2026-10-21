import json
import os
from pathlib import Path
from urllib.parse import quote


class SarifReporter:
    def generate_report(self, issues, output_file='report.sarif', analyzed_file='input.py'):
        ids = sorted({i['rule_id'] for i in issues})
        source_uri = quote(Path(os.path.relpath(Path(analyzed_file).resolve(), Path(output_file).resolve().parent)).as_posix(), safe='/.:')
        report = {'$schema': 'https://json.schemastore.org/sarif-2.1.0.json', 'version': '2.1.0',
                  'runs': [{'tool': {'driver': {'name': 'BUOI5-SAST', 'version': '1.0.0',
                           'rules': [{'id': r} for r in ids]}}, 'results': [
                      {'ruleId': i['rule_id'], 'level': {'high': 'error', 'medium': 'warning', 'low': 'note'}[i.get('severity', 'medium')],
                       'message': {'text': i['message']}, 'locations': [{'physicalLocation': {
                           'artifactLocation': {'uri': source_uri},
                           'region': {'startLine': i['lineno'], 'startColumn': i['col_offset'] + 1}}}]}
                      for i in issues]}]}
        Path(output_file).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
        return report
