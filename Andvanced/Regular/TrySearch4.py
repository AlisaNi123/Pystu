#!/usr/bin/env python
#coding=utf-8

import re

# str2 = "Hi~ The quick brown fox jumps over the lazy dog."
# searchObj = re.search(r'(.*) fox (.*?) .*', str2)
# print (searchObj.group())
# print (searchObj.groups())
# print (searchObj.group(1))
# print (searchObj.group(2))

str1 = "In Beijing test is No22 school."
obj1 = re.search(r'.* (\w+\d+) .*', str1)
print obj1.groups()