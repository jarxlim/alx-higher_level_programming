#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in range(len(my_list)):
        if idx < 0:
            return('none')
        else:
            return my_list[idx]
