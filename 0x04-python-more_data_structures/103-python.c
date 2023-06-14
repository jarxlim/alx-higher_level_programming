#include <stdio.h>
#include <Python.h>


/**
 * print_python_bytes - func print basic info about Python  objects
 * @p: python objects
 * Return: none
 **/
void print_python_bytes(PyObject *p)
{
  char *c;
  Py_ssize_t size, index;

  printf("[.] bytes object info\n");
  if (!PyBytes_Check(p))
    printf("  [ERROR] Invalid Bytes Object\n");
  else
    {
      PyBytes_AsStringAndSize(p, &c, &size);
      printf("  size: %lu\n", size);
      printf("  trying string: %s\n", c);
      if (size > 10)
	size = 10;
      else
	size++;
      printf("  first %lu bytes: ", size);
      for (index = 0; index < size - 1; index++)
	printf("%02x ", c[index] & 0xff);
      printf("%02x\n", c[size - 1] & 0xff);
    }
}


/**
 * print_python_list - func print  basic info on Python lists
 * @p: python object
 * Return: nothing
 **/
void print_python_list(PyObject *p)
{
  Py_ssize_t index;
  PyObject *in_list;

  if (PyList_Check(p))
    {
      printf("[*] Python list info\n");
     printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
      printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
      for (index = 0; index < PyList_Size(p); index++)
	{
	  in_list = PySequence_GetItem(p, index);
	  printf("Element %lu: %s\n", index,
		 in_list->ob_type->tp_name);
	  if (strcmp(in_list->ob_type->tp_name, "bytes") == 0)
	    print_python_bytes(in_list);
	}
    }
}
