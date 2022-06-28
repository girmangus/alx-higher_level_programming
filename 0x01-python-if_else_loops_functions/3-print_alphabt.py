#!/usr/bin/python3
for a in range(ord("a"), ord("z") + 1):
    if chr(a) is not "q" or chr(a) is not "e":
        print("{:s}".format(chr(a)), end="")
