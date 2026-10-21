import json
import os
import argparse
from pathlib import Path
from runtime_monitor import RuntimeMonitor
from memory_analyzer import MemoryAnalyzer
from network_traffic_analyzer import NetworkTrafficAnalyzer
from security_behavior_checker import SecurityBehaviorChecker
from virtual_sandbox import VirtualSandbox


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output')
    parser.add_argument('--summary', action='store_true')
    args = parser.parse_args()
    monitor = RuntimeMonitor(os.getpid())
    memory = MemoryAnalyzer()
    checker = SecurityBehaviorChecker().start()
    try:
        stdout, stderr = VirtualSandbox().run_isolated('echo Hello Sandbox')
    finally:
        checker.stop()
    report = dict(pid=os.getpid(), cpu_usage=monitor.get_cpu_usage(), memory_usage=monitor.get_memory_usage(),
                  open_files=[f.path for f in monitor.get_open_files()], memory=memory.check_memory_leaks(),
                  overflow_test=memory.check_overflow(2**64),
                  network={k: v._asdict() for k, v in NetworkTrafficAnalyzer().get_network_stats().items()},
                  suspicious_calls=checker.suspicious_calls(), sandbox=dict(stdout=stdout, stderr=stderr))
    if args.output:
        Path(args.output).write_text(json.dumps(report, indent=2), encoding='utf-8')
    if args.summary:
        print(f"PID={report['pid']} CPU={report['cpu_usage']}% RSS={report['memory_usage']} bytes")
        print('Memory observation:', json.dumps(report['memory']))
        print('Signed 64-bit overflow check for 2**64:', report['overflow_test'])
        for name, stats in report['network'].items():
            print(f"Network {name}: sent={stats['bytes_sent']} received={stats['bytes_recv']} bytes")
        print('Observed audit events:', json.dumps(report['suspicious_calls']))
        print('Sandbox stdout:', stdout.strip())
        print('Sandbox stderr:', repr(stderr))
        print('Full report:', args.output)
    else:
        print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
