import socket
import psutil
from network_traffic_analyzer import NetworkTrafficAnalyzer


def test_real_stats():
    stats = NetworkTrafficAnalyzer().get_network_stats()
    assert stats
    assert all(v.bytes_sent >= 0 and v.bytes_recv >= 0 for v in stats.values())


def test_real_loopback_traffic():
    before = psutil.net_io_counters().bytes_recv
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as receiver, socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender:
        receiver.bind(('127.0.0.1', 0))
        receiver.settimeout(2)
        sender.sendto(b'lab05' * 100, receiver.getsockname())
        assert len(receiver.recv(4096)) == 500
    assert psutil.net_io_counters().bytes_recv >= before
