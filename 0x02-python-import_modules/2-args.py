#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = len(sys.argv) - 1     # exclude (*.py) name from argument counter
    if counter == 0:
        print("{:d} {}".format(counter, "arguments."))
    elif counter == 1:
        print("{:d} {}".format(counter, "argument:"))
    else:
        print("{:d} {}".format(counter, "arguments:"))
    for i in range(counter):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
