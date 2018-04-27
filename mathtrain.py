#!/usr/bin/env python3

from math import pi

def printmutitable():
    for i in range(1,10):
        for j in range(1,i+1):
            print('{} X {} = {}'.format(j,i,i*j),end="\t")
        print('')

def circlearea(r):
    '''Caculate area for circle'''
    return (pi * int(r) ** 2)

if __name__ == '__main__':
    printmutitable()
    r = input('please input the radio length:')
    print (circlearea(r))
    print(circlearea.__doc__)
