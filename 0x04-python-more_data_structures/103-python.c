#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Print Python bytes object information
 * @p: Pointer to the Python object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes;
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;
    size = PyBytes_Size(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", bytes->ob_sval);

    printf("  first %zd bytes: ", size > 10 ? 10 : size);
    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x ", (unsigned char)bytes->ob_sval[i]);
    }
    printf("\n");
}

/**
 * print_python_list - Print Python list object information
 * @p: Pointer to the Python object
 */
void print_python_list(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t size, allocated, i;

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);
    allocated = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *elem = PyList_GetItem(p, i);
        printf("Element %zd: ", i);

        if (PyBytes_Check(elem))
        {
            printf("bytes\n");
            print_python_bytes(elem);
        }
        else if (PyFloat_Check(elem))
            printf("float\n");
        else if (PyTuple_Check(elem))
            printf("tuple\n");
        else if (PyList_Check(elem))
            printf("list\n");
        else if (PyLong_Check(elem))
            printf("int\n");
        else if (PyUnicode_Check(elem))
            printf("str\n");
        else
            printf("%s\n", elem->ob_type->tp_name);
    }
}
