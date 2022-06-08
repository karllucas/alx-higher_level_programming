#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary:
        del a_dictionary.get(value)
