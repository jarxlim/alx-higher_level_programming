#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if (number % 3) == 0:
            number = 'Fizz'
        elif (number % 5) == 0:
            number = 'Buzz'
        elif (number % 3 and number % 5) == 0:
            number = 'FizzBuzz'
        else:
            return (number)
    print("{:d}".format(number), end=' ')
