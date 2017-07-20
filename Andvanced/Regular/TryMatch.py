#!/usr/bin/env python
#coding=utf-8

import re

str1 = "www.testfan.cn"
str2 = "cnwww.testfan.cn"
obj1 = re.match("www", str1)
obj2 = re.match("cn", str2)
print (obj1)
print (obj2)

