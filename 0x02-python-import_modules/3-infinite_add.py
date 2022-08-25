#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    sum = 0
    for i in range(1, args):
        sum += int(sys.argv[i])
    print("{:d}".format(sum))
