import pytest
from memory_analyzer import MemoryAnalyzer


@pytest.mark.parametrize('value, expected', [(2**63-1, False), (2**63, True), (-2**63, False), (-2**63-1, True), (True, False), ('x', False)])
def test_signed_64_bit_bounds(value, expected):
    assert MemoryAnalyzer().check_overflow(value) is expected


def test_real_allocation_growth():
    analyzer = MemoryAnalyzer()
    allocation = bytearray(1024 * 1024)
    result = analyzer.check_memory_leaks()
    assert result['growth_bytes'] >= len(allocation)
