#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    inf_add = 0

    for i in range(1, len(argv)):
        inf_add += int(argv[i])
    print("{}".format(inf_add))
