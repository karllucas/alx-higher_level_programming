#!/usr/bin/python3
for alphabet in reversed(range(97, 123)):
    print("{:c}".format(alphabet if (alphabet % 2 == 0) else (alphabet - 32)), end='')
