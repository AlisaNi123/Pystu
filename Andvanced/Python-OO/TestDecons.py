#!/usr/bin/env python
#coding=utf-8

class MyClass():
    def __del__(self):
        print ("1")

    def test1(self):
        print ("2")

    def test2(self):
        print ("3")

    def __init__(self):
        print ("4")

myc = MyClass()
myc.test1()
myc.test2()