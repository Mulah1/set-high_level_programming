#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - print basic information about a Python list
 * @p: object to inspect
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t i;
	PyObject *item;

	if (p == NULL || p->ob_type != &PyList_Type)
		return;
	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", (long)list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", (long)list->allocated);
	for (i = 0; i < list->ob_base.ob_size; i++) {
		item = list->ob_item[i];
		printf("Element %ld: %s\n", (long)i, item->ob_type->tp_name);
		if (item->ob_type == &PyBytes_Type)
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - print basic information about a Python bytes object
 * @p: object to inspect
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	Py_ssize_t i, count;

	printf("[.] bytes object info\n");
	if (p == NULL || p->ob_type != &PyBytes_Type) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes = (PyBytesObject *)p;
	printf("  size: %ld\n", (long)bytes->ob_base.ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	count = bytes->ob_base.ob_size + 1;
	if (count > 10)
		count = 10;
	printf("  first %ld bytes:", (long)count);
	for (i = 0; i < count; i++)
		printf(" %02x", (unsigned char)bytes->ob_sval[i]);
	printf("\n");
}
