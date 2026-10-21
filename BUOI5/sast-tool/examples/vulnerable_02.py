"""Static analysis fixture; do not run with untrusted input."""
def dangerous_eval(user_input):
    return eval(user_input)


def read_file(filename):
    with open(filename, encoding='utf-8') as f:
        return f.read()


def execute_code(code):
    exec(code)
