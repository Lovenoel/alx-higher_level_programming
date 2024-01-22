#!/usr/bin/python3
"""module that prints an integer"""
import sys


def safe_print_integer_err(value):
        try:
                print("{:d}".format(value))
                return True
        except Exception as e:
                print("Exception:", e, file=sys.stderr)
                return False