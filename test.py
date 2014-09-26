#!/usr/bin/python
# -*- coding: utf8 -*-

from xml.etree import ElementTree

file = 'bin/collection_golden.txt'

f = open(file, 'r')
text = f.read()
f.close()

root = ElementTree.fromstring(text)
varNodes = root.getiterator('VAR')
for node in varNodes:
