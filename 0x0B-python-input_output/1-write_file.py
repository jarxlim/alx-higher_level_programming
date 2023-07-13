#!/usr/bin/python3
'''write_file function documentation'''
def write_file(filename="", text=""):
    '''function that writes a string to a text file (UTF8)'''
    with open(filename, "w", encoding='utf-8') as myFile:
        return myFile.write(text)
