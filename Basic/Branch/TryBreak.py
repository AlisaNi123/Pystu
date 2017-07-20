#!/usr/bin/env python
#coding=utf-8

#break
a = 100
while a>=0:
    if a == 95:
        break
    a -= 1
    print (a)

# continue
a = 10
while a > 0:
    if a == 6:
        a -= 1
        continue
    a -= 1
    print (a)