import ctypes


lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
i = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(i)
i = i + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(i)
i = []
lib.print_python_list_info(i)
i.append(0)
lib.print_python_list_info(i)
i.append(1)
i.append(2)
i.append(3)
i.append(4)
lib.print_python_list_info(i)
i.pop()
lib.print_python_list_info(i)
