# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

import logging

OUTPUT_DIR = 'out/'
BIN_DIR = 'bin/'
LOG_LEVEL = logging.DEBUG
LOG_LEVEL_FILE = logging.DEBUG
LOG_FILE = 'bin/fai.log'

PULL_INFO_SHELL = 'utils/pull_info.sh'

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