#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    a = 10
    b = 5
    print("{}, {}, result = {}".format(a, b, *(a, b)))
