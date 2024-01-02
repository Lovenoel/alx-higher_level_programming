#!/usr/bin/python3
<<<<<<< HEAD
def uppercase(str):
    for char in str:
        if 'a' <= char and 'z' >= char:
            else:
                char
                upperCase = chr(ord(char) - 32)
                print("{}".format((upperCase), end=" "))
=======
def uppercase(s):
    for char in s:
        # Convert each character to uppercase using ord() and chr()
        upper_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print(upper_char, end='')

    print()  # Print a new line after the uppercase string
>>>>>>> 70841e1b978ca1fd3d42b24ac334ab77f7fbd1ca
