#!/usr/bin/python3
def uppercase(str):
    for i in str:
        s = ord(str[i])
        if s >= 97 and s <= 123:
            s -= 32
        print("{}".format(chr(s)), end='')
    print()
