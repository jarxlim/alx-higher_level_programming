#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    '''The function will print a first name and a last nmae

    Args:
        first_name: this is the first name to print
        last_name: last name to print

    Raises:
        TypeError: if the first name and last name are not strings.

    '''

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
