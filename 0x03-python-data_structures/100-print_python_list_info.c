#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: pointer to PyObject (Python list)
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, allocated, i;
    PyObject *item;

    size = PyList_Size(p);
    allocated = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; ++i)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
