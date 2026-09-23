#include <Python.h>

/**
 * print_python_list_info - prints basic information about a Python list object
 * @p: Python object to inspect
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;

	if (p == NULL || !PyList_Check(p))
		return;

	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
