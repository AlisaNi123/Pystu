#!/usr/bin/env python
#coding=utf-8

import re

str1 = "In Beijing test-boring a No22school."
# if re.search(" \w*", str1):
#     print ("found!")
# else:
#     print ("Not found.")

if re.search("[a-zA-Z0-9 ]*", str1):
    print ("found!")
else:
    print ("Not found.")