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
HINT_UNCONNECTED_USB = '请将%s手机连接到PC.'#'Please connect the %s with PC by USB.'
HINT_PULL_SUCCESS = '成功获取%s手机信息.'#'Pull properties from %s successful.'
HINT_RAW_INPUT = '按回车(已就绪), 按其他(退出).'#'enter(aleady), else(exit)'
HINT_RAW_INPUT_EXIT = '你已退出, 再见.'#'You pressed any key to exit, bye!'

ERROR_FILE_NOT_EXIST = '文件不存在'#'File not exist!'
ERROR_DIR_NOT_EXIST = '文件夹不存在'#'Directory not exist!'

HINT_LACK_PARAMETER = '请添加参数:\n  -p [文件路径(可选)] 表示从golden手机中获取信息\n  -c [文件路径(可选)] 表示比较手机信息\n'
#'Please add parameters:\n  -p [golden path] pull golden info\n  -c [golden path] compare infomation\n'
HINT_INVALID_PARAMETER = '无效的参数'#'Invalid parameters!'
HINT_RESULT_OUTPUT_SUCCESS = '比较的详细结果已经输出至%s'#'The detail report have output successfully in [%s]'

INFO_DIFFERENT_VALUE = 'Golden手机和Sample手机的value不一致.' #Golden Phone and Sample Phone have different value.
INFO_NOT_IN_GOLDEN = 'Sample手机缺失的信息.' #Info exists in Golden but not in Sample.
INFO_NOT_IN_SAMPLE = 'Sample手机多余的信息.' #Info exists in Sample but not in Golden.
INFO_SYSPROP_DIFF = 'system property异常信息' #'system property difference'
INFO_SETTINGS_DIFF = 'settings 异常信息' #'settings difference'
INFO_RINGTONE_DIFF = 'ringtone 异常信息' #'ringtone difference'
INFO_FAI_RESULT = 'FAI结果' #'FAI result'
