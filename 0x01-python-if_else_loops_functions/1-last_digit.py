#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
if number < 6 and number != 0:
    print(f"Last digit of {number:d} is {num} and is less than 6 and not 0")
elif number > 5 and number != 0:
    print(f"Last digit of {number:d} is {num:d} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number:d} is {num:d} and is 0")
