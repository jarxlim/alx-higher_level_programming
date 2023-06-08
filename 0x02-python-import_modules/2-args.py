#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_no = len(argv) - 1

    if arg_no == 0:
        print("0 arguments.")
    elif arg_no == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_no))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
