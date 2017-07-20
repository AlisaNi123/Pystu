#!/usr/bin/env python
#coding=utf-8

class SecClass():
    attr1 = 10
    attr2 = "abc"

    def __init__(self, attr1, attr2):
        print ("in init.")
        self.setAttr1(attr1)
        self.setAttr2(attr2)

    def setAttr1(self, attr1):
        self.attr1 = attr1

    def getAttr1(self):
        return self.attr1

    def setAttr2(self, attr2):
        self.attr2 = attr2

    def getAttr2(self):
        return self.attr2

sec = SecClass(20, "Testfan")
aa = sec.getAttr1()
bb = sec.getAttr2()
print (aa, bb)