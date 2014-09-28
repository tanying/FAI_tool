# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

class FAIError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message 