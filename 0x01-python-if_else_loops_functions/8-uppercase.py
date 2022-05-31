#!/usr/bin/python3
def uppercase(str):
    for letter in range(len(str)):
        if ord(str[letter]) >= 97 and ord(str[letter]) <= 122:
            number = 32
        else:
            number = 0
        print("{:c}".format(ord(str[letter]) - number), end='')
    print()
