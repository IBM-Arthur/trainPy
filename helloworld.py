#!/usr/bin/env python

def helloworld(Name):
    print "hello world! "  + Name * 3


if __name__ == "__main__":
    name = raw_input('please input your name:')
    helloworld(name)
