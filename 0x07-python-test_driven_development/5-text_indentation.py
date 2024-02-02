#!/usr/bin/python3
""" a module that prints a text with 2 new lines after
each of these characters: ., ? and"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars_to_indent = {'.', '?', ':'}

    for char in text:
        if char in chars_to_indent:
            print()
            print()
        else:
            print(char, end='')
