#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a + 1, 10):
        print("{:d}".format(a), end='')
        if a == 8 and b == 9:
            print("{:d}".format(b), end='\n')
        else:
            print("{:d}".format(b), end=', ')
