from sast_tool.code_quality_checker import CodeQualityChecker


def test_branch_metrics():
    result = CodeQualityChecker().metrics('import os\ndef f(x):\n    if x and x > 1:\n        return 1\n    return 0')
    assert result['dependencies'] == 1
    assert result['functions'][0]['complexity'] == 3
    assert result['functions'][0]['nesting'] == 1


def test_long_function_flag(tmp_path):
    path = tmp_path / 'long.py'
    path.write_text('def f():\n' + '    x = 1\n' * 51)
    assert len(CodeQualityChecker().check(path)) == 1
