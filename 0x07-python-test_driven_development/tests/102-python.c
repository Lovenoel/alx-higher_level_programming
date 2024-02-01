#include <Python.h>

/**
 * print_python_string - Prints information about Python string objects
 * @p: Pointer to a Python object
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    wchar_t *unicode;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    unicode = PyUnicode_AsWideCharString(p, NULL);

    printf("  type: %s %s\n",
           (PyUnicode_IS_COMPACT_ASCII(p)) ? "compact" : "compact unicode object",
           (PyUnicode_IS_COMPACT_ASCII(p)) ? "ascii" : "unicode");
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", unicode);

    PyMem_Free(unicode);
}
