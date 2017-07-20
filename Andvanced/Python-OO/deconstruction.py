#!/usr/bin/env python
#coding=utf-8

class MyClass():
    def __init__(self):
        print ("1")

    def test(self):
        print ("2")

    def __del__(self):
        print ("3")

myc = MyClass()