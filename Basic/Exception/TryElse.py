#!/usr/bin/env python
#coding=utf-8

import math
try:
    fh = open("a.txt","r")
    fh.close()
except Exception as e:
    pass
else:
    print ("in else block.")