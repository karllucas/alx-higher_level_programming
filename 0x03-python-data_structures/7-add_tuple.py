#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a, tuple_b = 0, 1
    while tuple_a < 10:
        print(tuple_a)
        tuple_a, tuple_b = tuple_b, tuple_a + tuple_b
    print('{(:d, :d)}'.format(tuple_a, tuple_b))
