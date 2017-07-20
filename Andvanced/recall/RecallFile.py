#!/usr/bin/env python
#coding=utf-8

# fh = open("a.txt","r")
# fh.readlines()
# fh.close()

str1 = '''Testfan
is 
a good
school.
'''

fh = open("a.txt","w")
fh.write(str1)
fh.writelines()
fh.close()