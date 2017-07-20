#!/usr/bin/env python
#coding=utf-8

dict1 = {'a':1, 'b':2, 'c':3}
print dict1
dict2 = {v:k for k,v in dict1.items()}
print dict2