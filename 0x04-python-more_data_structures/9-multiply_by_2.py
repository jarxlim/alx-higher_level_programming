#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}
    for keys in a_dictionary.keys():
        res[keys] = a_dictionary[keys] * 2
    return res
