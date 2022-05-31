#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
for i in number:
    intro_string = print(f'Last digit of {number} is {i}')
    if i > 5:
        print(f'{intro_string} and is greater than 5')
    elif i == 0:
        print(f'{intro_string} and is 0')
    elif i < 6 && i != 0:
        print(f'{intro_string} and is less than 6 and not 0')
