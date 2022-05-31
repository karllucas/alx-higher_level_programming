#!/usr/bin/python3
def uppercase(str):
    for letter in range(len(str)):
        if ord(letter) >= 97 and  ord(letter) <= 122:
            number = 32
        else:
            number = 0
        print("{:c}".format(ord(letter) - number), end='')
    print()
