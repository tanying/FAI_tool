# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

import logging

OUTPUT_DIR = 'out/'
BIN_DIR = 'bin/'
LOG_LEVEL = logging.DEBUG
LOG_LEVEL_FILE = logging.DEBUG
LOG_FILE = 'bin/fai.log'

PULL_INFO_SHELL = 'utils/pull_info.sh'

GOLDEN_PROPERTY = 'bin/property_golden.txt'
SAMPLE_PROPERTY = 'bin/property_sample.txt'

GOLDEN_COLLECTION = 'bin/collection_golden.txt'
SAMPLE_COLLECTION = 'bin/collection_sample.txt'

PULL_SUCCESS_FLAG = False

PROPERTY_COMPARE_RESULT = 'out/compare_result.txt'