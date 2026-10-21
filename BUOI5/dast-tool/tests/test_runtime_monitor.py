import os
import psutil
import pytest
from runtime_monitor import RuntimeMonitor


def test_real_process():
    monitor = RuntimeMonitor(os.getpid())
    assert monitor.get_cpu_usage() >= 0
    assert monitor.get_memory_usage() > 0
    assert isinstance(monitor.get_open_files(), list)


def test_missing_process():
    with pytest.raises(psutil.NoSuchProcess):
        RuntimeMonitor(2147483647)
