#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("{} arguements.".format(num - 1))
    elif num == 2:
        print("{} arguement:".format(num - 1))
    else:
        print("{} arguements:".format(num - 1))

    for arguement in range(1, num):
        print("{}: {}".format(argument, sys.argv[arguement]))
