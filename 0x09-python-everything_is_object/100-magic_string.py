#!/usr/bin/python3
# 100-magic_string.py
"""Returns a string n times of iteration."""


def magic_string():
    """Recieves string and creates multiple duplicates."""
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("Holberton, " * (magic_string.n - 1) + "Holberton")
