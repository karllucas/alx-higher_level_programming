#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
     try:
        res = fct(*args)
        return res
     except Exception as i:
        print("Exception: {}".format(i), file=sys.stderr)
        return None
