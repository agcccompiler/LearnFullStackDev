#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
def say_hello():
    args = sys.argv
    if len(args) == 1:
        print('Hello from Fun.py!')
    elif len(args) == 2:
        print(f'Hello, {args[1]} from Fun.py!')
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    say_hello()
