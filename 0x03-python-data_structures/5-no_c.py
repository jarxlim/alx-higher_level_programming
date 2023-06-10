#!/usr/bin/python3
def no_c(my_string):
    for char in my_string:
        if char == chr(67) or char == chr(99):
            my_string.remove(char)
            return my_string
