#!/usr/bin/python3
"""
Append to a file module
"""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
