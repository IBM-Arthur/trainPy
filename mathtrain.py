#!/usr/bin/env python3

def printmutitable():
    for i in range(1,10):
        for j in range(1,i+1):
            print('{} X {} = {}'.format(j,i,i*j),end="\t")
        print('')
