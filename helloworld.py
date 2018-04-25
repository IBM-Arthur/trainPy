#!/usr/bin/env python
from math import pi

def helloworld(Name):
    print "hello world! "  + Name * 3

def circlearea(r):
    return pi * r ** 2


if __name__ == "__main__":
    name = raw_input('please input your name:')
    helloworld(name)

    r = raw_input('please input the radio length:')
    circlearea(r)
