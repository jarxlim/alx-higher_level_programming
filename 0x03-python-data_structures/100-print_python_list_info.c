#include "Python.h"
/**
 * print_python_list_info - information about python objects
 * @p: PyObject pointer to print info about
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t index, py_list;
	PyObject *obj;
	const char *obj_type;
	PyListObject *list_object;

	list_object = (PyListObject *)p;
	py_list = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int) py_list);
	printf("[*] Allocated = %d\n", (int)list_object->allocated);
	for (index = 0; index < py_list; index++)
	{
		item = PyList_GetItem(p, index);
		obj_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", (int) index, obj_type);
	}
}
