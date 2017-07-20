#!/usr/bin/env python
#coding=utf-8

import re

str1 = " t1estfan is a good school. test"

if re.search("test", str1):
    print ("find string starts with \"test\".")
else:
    print ("Cannot find.")

# if re.match("test", str1):
#     print ("find string starts with \"test\".")
# else:
#     print ("Cannot find.")

# if re.search("school\.$", str1):
#     print ("find string ends with \"school\.\".")
# else:
#     print ("Cannot find.")