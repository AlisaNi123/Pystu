#!/usr/bin/env python
#coding=utf-8

fh = open("Testfan","r")
while True:
    line = fh.readline()
    if not line:
        break
    print line.strip("\n")
fh.close()