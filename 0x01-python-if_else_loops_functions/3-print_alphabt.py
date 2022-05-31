#!/usr/bin/python3
for alphabet in range(97, 123):
    if alphabet == 113:
        break
    elif alphabet == 101:
        break
    else:
        print("{:c}".format(alphabet), end='')
