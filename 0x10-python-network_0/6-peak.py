#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """highest value in a list of unsorted integers"""

    my_list = list_of_integers

    if my_list:
        my_list.sort()
        return my_list[-1]
    else:
        return None
