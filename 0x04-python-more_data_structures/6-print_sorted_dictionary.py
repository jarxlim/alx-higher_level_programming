#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortKeys = sorted(a_dictionary.keys())
    for i in sortKeys:
        print("{}: {}".format(i, a_dictionary[i]))
