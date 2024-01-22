import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s)
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00'
lib.print_python_bytes(b)
b = b'What does the \'b\' character do in front of a string literal?'
lib.print_python_bytes(b)
i = [b'Hello', b'World']
lib.print_python_list(i)
del i[1]
lib.print_python_list(i)
i = i + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
lib.print_python_list(i)
i = []
lib.print_python_list(i)
i.append(0)
lib.print_python_list(i)
i.append(1)
i.append(2)
i.append(3)
i.append(4)
lib.print_python_list(i)
i.pop()
lib.print_python_list(i)
i = ["Holberton"]
lib.print_python_list(i)
lib.print_python_bytes(i)
