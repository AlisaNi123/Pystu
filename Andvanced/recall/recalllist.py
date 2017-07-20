#!/usr/bin/env python
#coding=utf-8

list1 = [1, "abc", 1.1, 'd']
list1[1] = 22
list2 = [4,5,6]
list1.append("def")
list1.append(1)
list1.append(list2)
print list1.count(1)
print (list1)
print ("==============================")

print (list1[0:3]) #slice