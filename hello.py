#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jincheng Guo'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
    print(f"platform: {sys.platform}")
    print(f"version:{sys.version}")
    print(f"author:{__author__}")
    print(f"name:{__name__}")
    print("modules path: %s" %(sys.path))
