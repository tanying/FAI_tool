# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

class Info(object):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
    def show(self):
        result = self.message
        type= sys.getfilesystemencoding()
        #change string to system encoding for messy code
        result = result.decode('utf-8').encode(type)
        print result