import pytest
from virtual_sandbox import VirtualSandbox


def test_real_child_process():
    stdout, stderr = VirtualSandbox().run_isolated('echo Hello Sandbox')
    assert stdout.strip() == 'Hello Sandbox'
    assert stderr == ''


@pytest.mark.parametrize('command', ['whoami', 'echo a & whoami', 'echo %PATH%', None, 'echo x\ny'])
def test_reject_command_injection(command):
    with pytest.raises(ValueError):
        VirtualSandbox().run_isolated(command)
