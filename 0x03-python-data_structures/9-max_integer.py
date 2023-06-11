#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        sortedlist = sorted(my_list, reverse=True)
        return(sortedlist[0])
