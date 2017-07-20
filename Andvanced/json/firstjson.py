#!/usr/bin/env python
#coding=utf-8

import json

dict1 = {
"Students":[
{"firstname":"John","lastname":"Doe"},
{"firstname":"Mary","lastname":"Tran"},
{"firstname":"Peter","lastname":"Jones"}
]}

j = json.dumps(dict1)
print (type(j))
print (j)
print ("=======================")
s = json.loads(j)
print (type(s))
print (s)