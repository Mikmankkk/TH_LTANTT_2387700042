import json
from sast_tool.sarif_reporter import SarifReporter


def test_report_locations_and_levels(tmp_path):
    path = tmp_path / 'report.sarif'
    issue = dict(rule_id='test', message='review', severity='high', lineno=4, col_offset=2)
    report = SarifReporter().generate_report([issue], path, 'examples/test.py')
    assert json.loads(path.read_text()) == report
    finding = report['runs'][0]['results'][0]
    assert finding['level'] == 'error'
    assert finding['locations'][0]['physicalLocation']['region'] == dict(startLine=4, startColumn=3)


def test_empty_report(tmp_path):
    report = SarifReporter().generate_report([], tmp_path / 'empty.sarif')
    assert report['version'] == '2.1.0'
    assert report['runs'][0]['results'] == []
