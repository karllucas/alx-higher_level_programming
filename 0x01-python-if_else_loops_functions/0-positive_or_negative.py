#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for i in number:
        if i > 0:
		 print('is positive')
        elif i == 0:
		print('is zero')
	elif i < 0:
		print('is negative')
