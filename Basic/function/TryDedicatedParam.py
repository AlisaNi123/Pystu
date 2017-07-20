#!/usr/bin/env python
#coding=utf-8

# 固定参数的函数
def func6(b, c, a=10):
    return a+b+c

print (func6(10,20))
print (func6(10, 20, 30))
