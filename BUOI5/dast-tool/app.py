import os
import subprocess
from flask import Flask, jsonify, request
from runtime_monitor import RuntimeMonitor
from memory_analyzer import MemoryAnalyzer
from network_traffic_analyzer import NetworkTrafficAnalyzer
from security_behavior_checker import SecurityBehaviorChecker
from virtual_sandbox import VirtualSandbox

app = Flask(__name__)
memory_analyzer = MemoryAnalyzer()
checker = SecurityBehaviorChecker()


@app.get('/api/monitor')
def monitor():
    rm = RuntimeMonitor(os.getpid())
    return jsonify(cpu_usage=rm.get_cpu_usage(), memory_usage=rm.get_memory_usage(), open_files=[f.path for f in rm.get_open_files()])


@app.get('/api/memory')
def memory():
    return jsonify(memory_leaks=memory_analyzer.check_memory_leaks(), overflow_test=memory_analyzer.check_overflow(2**64))


@app.get('/api/network')
def network():
    return jsonify(network_stats={k: v._asdict() for k, v in NetworkTrafficAnalyzer().get_network_stats().items()})


@app.get('/api/security')
def security():
    return jsonify(suspicious_calls=checker.suspicious_calls())


@app.post('/api/sandbox')
def sandbox():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not isinstance(data.get('command'), str):
        return jsonify(error='Expected JSON object with string command'), 400
    checker.start()
    try:
        stdout, stderr = VirtualSandbox().run_isolated(data['command'])
        return jsonify(stdout=stdout, stderr=stderr)
    except ValueError as exc:
        return jsonify(error=str(exc)), 400
    except subprocess.TimeoutExpired:
        return jsonify(error='Demo timed out'), 408
    finally:
        checker.stop()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False, threaded=False)
