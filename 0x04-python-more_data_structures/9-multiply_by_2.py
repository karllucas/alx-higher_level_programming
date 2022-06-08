#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    for value in a_dictionary:
        new_d[value] = a_dictionary[value] * 2
    return new_d
