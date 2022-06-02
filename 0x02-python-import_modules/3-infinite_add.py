#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for j in range(1, len(argv)):
        sum += int(argv[j])
    print("{}".format(j))
