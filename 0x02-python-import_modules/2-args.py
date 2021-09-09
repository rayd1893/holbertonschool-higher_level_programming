#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    lenArg = len(sys.argv) - 1
    text = "arguments"
    sig = ":"
    argv = sys.argv

    if lenArg == 0:
        sig = "."

    if lenArg == 1:
        text = "argument"

    print("{:d} {}{}".format(lenArg, text, sig))

    for i in range(1, lenArg + 1):
        print("{:d}: {}".format(i, argv[i]))
