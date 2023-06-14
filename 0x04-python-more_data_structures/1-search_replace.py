#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list.copy()
    for i in range(len(newlist)):
        if newlist[i] == search:
            newlist[i] = replace
    return newlist
