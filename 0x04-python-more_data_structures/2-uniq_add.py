#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0

    uniq = set(my_list)
    for num in uniq:
        result = result + num
    return result
