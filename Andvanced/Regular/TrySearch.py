#!/usr/bin/env python
#coding=utf-8

import re

str1 = "www.testfan.cn"
obj1 = re.search("www", str1)
obj2 = re.search("cn", str1)
print (obj1)
print (obj2)

if re.search("cn", str1):
    print "xxxxxxx"