#!/usr/bin/env python
#coding=utf-8

import re

str1 = "test is a                     good     school."
if re.search("a\s*good\s*", str1):
    print "find space and good."
