#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_digit = num_str[-1]
if number >= 0:
    last_digit = int(last_digit)
elif number > 0:
    last_digit = 0 - int(last_digit)
print(f"Last digit of {number} is {last_digit}", end = " ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
elif last_digit < 6 and last_digit != 0:
    print("and is less than 6 and not 0")
