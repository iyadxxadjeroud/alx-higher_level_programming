#!/usr/bin/python3
import sys

argument = len(sys.argv) - 1
if argument == 0:
    print(".")
elif argument == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(argument))
for i in range(argument):
    print("{}: {}".format(i + 1, sys.argv[i +1]))
