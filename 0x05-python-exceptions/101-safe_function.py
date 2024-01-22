#!/usr/bin/python3
"""module  that executes a function safely"""
import sys


def safe_function(fct, *args):
        try:
                result = fct(*args)
                return result
        except Exception as e:
                print("Exception:", e, file=sys.stderr)
        return None