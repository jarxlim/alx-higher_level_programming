#!/usr/bin/python3
'''module contains a class MyList that inherits from list'''


class MyList(list):
    '''a class MyList that inherits from list'''
    def print_sorted(self):
        '''prints the sortrd list'''
        print(sorted(self))
