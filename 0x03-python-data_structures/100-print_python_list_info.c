#include "Python.h"
/**
 * print_python_list_info - info about python objects
 * @p: PyObject pointer to print info about
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t index, py_list_size;
	PyObject *item;
	const char *item_type;
	PyListObject *list_object_cast;

	list_object_cast = (PyListObject *)p;
	py_list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int) py_list_size);
	printf("[*] Allocated = %d\n", (int)list_object_cast->allocated);
	for (index = 0; index < py_list_size; index++)
	{
		item = PyList_GetItem(p, index);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) index, item_type);
	}
}
