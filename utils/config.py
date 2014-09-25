# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

import logging

OUTPUT_DIR = 'out/'
LOG_LEVEL = logging.DEBUG
LOG_LEVEL_FILE = logging.DEBUG
LOG_FILE = 'bin/goldenInfoCmp.log'

PULL_INFO_SHELL = 'utils/pull_info.sh'

GOLDEN_PROPERTY = 'bin/property_golden.txt'
SAMPLE_PROPERTY = 'bin/property.txt'

PULL_SUCCESS_FLAG = False

PROPERTY_COMPARE_RESULT = 'out/property_compare_result.txt'