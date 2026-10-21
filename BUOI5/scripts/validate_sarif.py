import json
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parents[1]
schema = json.loads((ROOT / 'reports/sarif-schema-2.1.0.json').read_text(encoding='utf-8'))
for path in sorted((ROOT / 'reports').glob('*.sarif')):
    report = json.loads(path.read_text(encoding='utf-8'))
    jsonschema.validate(report, schema)
    results = report['runs'][0]['results']
    print(f'{path.name}: SARIF 2.1.0 schema PASS; findings={len(results)}')
    for result in results:
        location = result['locations'][0]['physicalLocation']
        print(f"  {result['level']} {result['ruleId']} line={location['region']['startLine']} {result['message']['text']}")
