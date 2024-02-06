#!/usr/bin/python3
"""A module a function that inserts a line of text to a file, after each line
 containing a specific string (see example)"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line containing a specific
    string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

if __name__ == "__main__":
    filename = "append_after_100.txt"
    search_string = "Python"
    new_string = "\"C is fun!\"\n"
    append_after(filename, search_string, new_string)
