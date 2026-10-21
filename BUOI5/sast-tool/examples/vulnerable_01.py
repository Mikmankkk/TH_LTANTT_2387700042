"""Intentional lab fixture: fake credential, never a real account."""
password = 'DEMO_ONLY_NOT_A_REAL_PASSWORD'
import pickle


def unsafe_func(data):
    return eval(data)


def safe_func():
    print('Hello world!')
