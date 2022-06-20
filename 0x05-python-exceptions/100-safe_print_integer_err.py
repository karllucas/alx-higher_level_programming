#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        print("Exception: {:d}".format(value))
        return False
