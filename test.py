#!/usr/bin/python
# -*- coding: utf8 -*-

def filter_xml_tag(ltag, string):
    string = string.replace(ltag, '')
    rtag = '</' + ltag[1:]
    string = string.replace(rtag, '')
    string = string.replace('\n', '')
    return string

SETTINGS_KEY_TAG = '<golden.settings.title>'
SETTINGS_VAL_TAG = '<golden.settings.content>'

RINGTONE_KEY_TAG = '<golden.ringtone.title>'
RINGTONE_VAL_TAG = '<golden.ringtone.content>'

file = 'bin/collection_golden.txt'

sdict = {}
rdict = {}

f = open(file, 'r')
flist = f.readlines()
f.close()

key = ''
count = 0
for item in flist:
    mod = count % 2
    if mod == 0:
        print 
        if item[:len(SETTINGS_KEY_TAG)] == SETTINGS_KEY_TAG:
            key = filter_xml_tag(SETTINGS_KEY_TAG, item)
        elif item[:len(RINGTONE_KEY_TAG)] == RINGTONE_KEY_TAG:
            key = filter_xml_tag(RINGTONE_KEY_TAG, item)
    else:
        if item[:len(SETTINGS_VAL_TAG)] == SETTINGS_VAL_TAG:
            val = filter_xml_tag(SETTINGS_VAL_TAG, item)
            sdict[key] = val
        elif item[:len(RINGTONE_VAL_TAG)] == RINGTONE_VAL_TAG:
            val = filter_xml_tag(RINGTONE_VAL_TAG, item)
            rdict[key] = val

    count += 1

print sdict
print rdict