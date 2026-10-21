from sast_tool.ast_analyzer import ASTAnalyzer


def test_unsafe_calls_and_aliases():
    result = ASTAnalyzer().analyze('import os as o\no.system("echo x")\neval("1")\nexec("x=1")')
    assert len(result) == 3
    assert result[0]['lineno'] == 2


def test_comments_and_strings_are_not_calls():
    assert ASTAnalyzer().analyze('# eval(x)\ns = "exec(x)"') == []


def test_shell_true():
    assert len(ASTAnalyzer().analyze('import subprocess\nsubprocess.run("x", shell=True)')) == 1


def test_syntax_error():
    import pytest
    with pytest.raises(SyntaxError):
        ASTAnalyzer().analyze('def (')
