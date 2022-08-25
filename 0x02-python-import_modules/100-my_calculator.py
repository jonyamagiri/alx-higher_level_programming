#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = argv[2]
    if ops == "+":
        sum = add(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, sum))
    elif ops == "-":
        sub = sub(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, sub))
    elif ops == "*":
        mul = mul(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, mul))
    elif ops == "/":
        div = div(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, div))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
