#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    num = number % 10
    num *= -1
    number *= -1
else:
    num = number % 10
if num < 6 and num != 0:
    print(f"Last digit of {number:d} is {num} and is less than 6 and not 0")
elif num > 5 and num != 0:
    print(f"Last digit of {number:d} is {num:d} and is greater than 5")
elif num == 0:
    print(f"Last digit of {number:d} is {num:d} and is 0")
