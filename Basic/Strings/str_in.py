#!/usr/bin/env python
#coding=utf-8

str1 = "testfan"
str2 = "TestFan"

if "es" in str1:
    print "Found!!"
else:
    print "Not found!"

if "te".lower() in str2.lower():
    print "Found!!"
else:
    print "Not found!"