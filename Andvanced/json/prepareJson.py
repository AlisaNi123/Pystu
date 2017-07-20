#!/usr/bin/env python
#coding=utf-8

list1 = [1,2,3]
dict1 = {"numbers": list1}
dict1["bool"] = True
dict1[100] = "Python"
dict2 = {'a':10,'b':20, 'c':30,'d':40}
dict1["dict2"] = dict2
print (dict1)
print (dict1["numbers"])
print (dict1["numbers"][0])
print (dict1["dict2"]["d"])