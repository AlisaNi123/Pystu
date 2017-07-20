#!/usr/bin/env python
#coding=utf-8

try:
    1 / 0
except BaseException as e:
    print e
else:
    print("in elseblock")
finally:
    print ("in finally block...")
