#!/usr/bin/env python
#coding=utf-8

class MyParent0():
    def __init__(self):
        print ("I'm parent class.")

class MyParent1():
    def __init__(self):
        print ("I'm parent class.")

class MyChild(MyParent0,MyParent1):
    def __init__(self):
        print ("I'm child class.")

myc = MyChild()