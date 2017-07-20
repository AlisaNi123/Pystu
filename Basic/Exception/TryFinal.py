#!/usr/bin/env python
#coding=utf-8

t1 = (1,2,3)
try:
    t1[1] = 100
except Exception as e1:
    print ("in first exception.")
    print (e1)
finally:
    print ("in finally block.")
