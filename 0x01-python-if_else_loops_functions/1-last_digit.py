#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10 if number > 10 else number % -10
if mod > 5:
    print(f"The last digit of {number} is {mod} and is greater than 5")
elif mod == 0:
    print(f"The last digit of {number} is {mod} and is zero")
else:
    print(f"The last digit of {number} is {mod} and is less than 6 and not 0 ")
