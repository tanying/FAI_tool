# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

import os
import sys
import log
import json
import config
import commands

logger = log.getLogging('utils.py')

def get_confirm_result(string):
    return (string.lower() == 'y' or string.lower() == 'yes') and True or False
