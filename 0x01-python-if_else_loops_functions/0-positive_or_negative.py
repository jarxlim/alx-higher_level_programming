#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for num in range(-10, 10):
    if num > 0:
        print("{} is positive".format(num))
    elif num == 0:
        print("{} is zero".format(num))
    else:
        print("{} is negative".format(num))
