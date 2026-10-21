import ast
import os


def parse_data(text):
    return ast.literal_eval(text)


def credential():
    return os.environ.get('LAB_PASSWORD')
