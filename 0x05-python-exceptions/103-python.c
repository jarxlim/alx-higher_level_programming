#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>
#include <Python.h>
#include <stdio.h>

/**
 * float_printer - print float objects
 * @p: pointer to PyObject
 */
void float_printer(PyObject *p)
{
	double dd;
	char *c = NULL;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}
	dd = ((PyFloatObject *)(p))->ob_fval;
	c = PyOS_double_to_string(dd, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", c);
	fflush(stdout);
}

/**
 * bytes_printer - print sbytrs objrct
 * @p: pointer to PyObject
 */
void bytes_printer(PyObject *p)
{
	size_t index, byte;
	char *string = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}
	string = ((PyBytesObject *)(p))->ob_sval;
	byte = PyBytes_Size(p);
	printf("  size: %ld\n", byte);
	printf("  trying string: %s\n", string);
	if (byte >= 10)
		byte = 10;
	else
		byte++;
	printf("  first %ld bytes: ", byte);
	for (index = 0; index < byte - 1; index++)
		printf("%02hhx ", str[index]);
	printf("%02hhx", str[index]);
	printf("\n");
	fflush(stdout);
}

/**
 * list_printer - print Python lists
 * @p: pointer to PyObject
 */
void list_printer(PyObject *p)
{
	size_t index, alloc, len;
	const char *dataType;
	PyListObject *list;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}
	list = (PyListObject *)p;
	len = PyList_GET_SIZE(p);
	alloc = list->alloc;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %li\n", alloc);
	for (index = 0; index < len; index++)
	{
		dataType = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %li: %s\n", i, dataType);
		if (strcmp(dataType, "bytes") == 0)
			bytes_printer(list->ob_item[index]);
		else if (strcmp(dataType, "float") == 0)
			float_printer(list->ob_item[index]);
	}
	fflush(stdout);}
