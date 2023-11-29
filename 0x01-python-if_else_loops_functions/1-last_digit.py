#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = int(str(number)[-1])
format_message = f"Last digit of {number} is"

if last_digit > 5:
    print(f"{format_message} {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{format_message} {last_digit} and is 0")
elif last_digit != 0 and last_digit < 6:
    print(f"{format_message} {last_digit} and is less than 6 and not 0")
