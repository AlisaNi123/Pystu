#!/usr/bin/env python
#coding=utf-8

import re

str1 = '''files = 1000
student = 128
size = 1024
Mem = 222G
HD = 512G
Mem = 4GB
HD = 1024TB
'''

aa = re.findall('Mem = (\d+\w+)',str1)
bb = re.findall('(\w+) = 1024.*', str1)
print aa
print bb