#!/usr/bin/env python
#coding=utf-8

import xml.dom.minidom
# SAX

DOMTree = xml.dom.minidom.parse("collection.xml")
cc = DOMTree.documentElement

dramas = cc.getElementsByTagName("drama")

for drama in dramas:
    print "********drama********"
    if drama.hasAttribute("title"):
        print "Title: %s" % drama.getAttribute("title")
    try:
        type = drama.getElementsByTagName('type')[0]
    except:
        print ("no type...")
    else:
        print "Type: %s" % type.childNodes[0].data