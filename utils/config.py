# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

#import logging

OUTPUT_DIR = 'out/'
BIN_DIR = 'bin/'
# LOG_LEVEL = logging.DEBUG
# LOG_LEVEL_FILE = logging.DEBUG
# LOG_FILE = 'bin/fai.log'

GOLDEN_PROPERTY = 'property_golden.txt'
SAMPLE_PROPERTY = 'property_sample.txt'

GOLDEN_COLLECTION = 'collection_golden.txt'
SAMPLE_COLLECTION = 'collection_sample.txt'

SETTINGS_KEY_TAG = '<golden.settings.title>'
SETTINGS_VAL_TAG = '<golden.settings.content>'

RINGTONE_KEY_TAG = '<golden.ringtone.title>'
RINGTONE_VAL_TAG = '<golden.ringtone.content>'

PULL_SUCCESS_FLAG = False

PROPERTY_COMPARE_RESULT = 'compare_result.txt'

#string
HINT_UNCONNECTED_USB = 'Please connect the %s with PC by USB.'
HINT_PULL_SUCCESS = 'Pull properties from %s successful.'
HINT_RAW_INPUT = 'enter(aleady), else(exit)'
HINT_RAW_INPUT_EXIT = 'You pressed any key to exit, bye!'

ERROR_FILE_NOT_EXIST = 'File not exist!'
ERROR_DIR_NOT_EXIST = 'Directory not exist!'

HINT_LACK_PARAMETER = 'Please add parameters:\n  -p [golden path] pull golden info\n  -c [golden path] compare infomation\n'
HINT_INVALID_PARAMETER = 'Invalid parameters!'