#!/usr/bin/env python
#coding=utf-8

dict1 = {}
str1 = "testfan is a good school testfan is good"
res = str1.split(" ")
# print (res) 
for s in res:
    # print (s)
    if dict1.has_key(s):
        dict1[s] += 1
    else:
        dict1[s] = 1
print dict1