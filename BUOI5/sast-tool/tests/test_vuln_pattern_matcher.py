from sast_tool.vuln_pattern_matcher import VulnPatternMatcher


def test_credentials_and_pickle():
    issues = VulnPatternMatcher().match("password = 'DEMO'\nimport pickle")
    assert {i['rule_id'] for i in issues} == {'hardcoded-secret', 'unsafe-import'}


def test_no_false_comment_secret():
    assert VulnPatternMatcher().match('# password = "x"\npassword = None') == []


def test_custom_pattern_coordinates():
    result = VulnPatternMatcher([dict(id='custom', pattern='danger', message='review')]).match('x=1\n# danger')
    assert (result[0]['lineno'], result[0]['col_offset']) == (2, 2)
