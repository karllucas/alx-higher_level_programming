#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i in range(my_list):
        if my_list[i] % 2 != 0:
            return False
        elif my_list[i] % 2 == 0:
            return True
    return my_list
