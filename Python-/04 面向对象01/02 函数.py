#!/usr/bin/python3
# -*- coding:utf-8 -*-
def print_my(*args,**kwargs):
    for i in args:
        print(kwargs)
        for item in kwargs.values():
            return print(i,item,end='\t')

print_my('hello',hello=1)