#!/usr/bin/env python3

# Title: sillySentence 300
# Author: Arthur
# This is interactive game base on user input
import os

def printWelcome():
    print('*' * 48)
    print('* Welcome to the Silly Sentence Generator 3000 *')
    print('*' * 48)

def sayhello(name):
    print("Hello",name,"! let's make a silly sentence!" )
    voice = 'say Welcome to silly sentence' + ' ' + name
    os.system(voice)
if __name__ == '__main__':
    printWelcome()
    name = input('Please input your name:')
    sayhello(name.capitalize())
