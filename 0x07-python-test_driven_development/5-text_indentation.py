#!/usr/bin/python3
''' this module contains function that prints a text with 2 new lines
 after each of these characters: ., ? and :'''


def text_indentation(text):

    '''
    this function prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text: a string of chars

    Raise:
        TypeError: if text is not a string
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    for char in text:
        if count == 0:
            if char == ' ':
                continue
            else:
                count = 1
        if count == 1:
            if char == '?' or char == '.' or char == ':':
                print(char, end='\n')
                count = 0
            else:
                print(char, end="")
