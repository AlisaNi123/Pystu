#!/usr/bin/env python
#coding=utf-8

def myfun1(b,a=10, *var):
    print "Hello"
    print (a)
    print (a,b)

myfun1(10)
print()
print (1,2,3,4,5,6)