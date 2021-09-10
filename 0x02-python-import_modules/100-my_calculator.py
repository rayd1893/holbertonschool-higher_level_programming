#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sig = sys.argv[2]

    list = {add:"+", sub:"-", mul:"*", div:"/"}

    for fun, op in list.items():
        if op == sig:
            print("{:d}".format(fun(a, b)))
            sys.exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
