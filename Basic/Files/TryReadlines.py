#!/usr/bin/env python
#coding=utf-8

fh = open("Testfan","r")
lines = fh.readlines()
for line in lines:
    print line.strip("\n") #.strip("\n") #.replace("\n","")
fh.close()