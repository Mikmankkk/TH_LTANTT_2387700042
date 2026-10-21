from security_behavior_checker import SecurityBehaviorChecker


def test_observes_real_execution_and_stop():
    checker = SecurityBehaviorChecker().start()
    try:
        exec(compile('value = 42', '<lab>', 'exec'), {})
        assert any(e['event'] == 'exec' for e in checker.suspicious_calls())
    finally:
        checker.stop()
    count = len(checker.events)
    exec('pass')
    assert len(checker.events) == count
    checker.start()
    try:
        exec('pass')
    finally:
        checker.stop()
    assert len(checker.events) == count + 1
