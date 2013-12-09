#!/usr/bin/env python
import sys


def doge(args):
    print "wow, very arguments:"
    for num, arg in args.items():
        print " {}: {}".format(num, arg)
    print "such python"

if __name__ == '__main__':
    arguments = dict(zip(range(len(sys.argv)), sys.argv))
    doge(arguments)
