#!/usr/bin/env python
#coding=utf-8

class Person():
    Name = ""
    Sex = "Male"
    __Age = 0

    def __init__(self, name, sex, age):
        self.Name = name
        self.Sex = sex
        self.__Age = age

Tom = Person("Tom", "male", 30)
print (Tom.Name)
print (Tom.Sex)
print (Tom.__Age)