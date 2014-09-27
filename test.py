#!/usr/bin/python
# -*- coding: utf8 -*-

#!/usr/bin/python
# -*- coding: utf8 -*-

file = 'bin/collection_golden.txt'

f = open(file, 'r')
flist = f.readlines()
f.close()

for item in flist:
    print item
    print flist.index(item)