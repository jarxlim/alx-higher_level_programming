#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and num % 5 == 0:
            number = 'FizzBuzz'
        elif number % 5 == 0:
            number = 'Buzz'
        elif number % 3 == 0:
            number = 'Fizz'
        else:
            return (number)
    print("{:d}".format(number), end=' ')
