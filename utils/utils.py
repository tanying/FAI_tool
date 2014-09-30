# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

import os
import sys
#import log
import json
import commands
from config import *

#logger = log.getLogging('utils.py')

def filter_brackets(string):
    return string[1:-1]

def filter_xml_tag(ltag, string):
    string = string.replace(ltag, '')
    rtag = '</' + ltag[1:]
    string = string.replace(rtag, '')
    string = string.replace('\n', '')
    return string

def is_pull_aready(path):
    cmd = 'adb shell ls /sdcard/ | grep %s' % path
    s = os.system(cmd)
    if s == 0:
        return True
    else:
        return False

def change_file_to_dict(filepath):
    fdict = {}
    f = open(filepath, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        else:
            line_list = line.split(':')
            key = filter_brackets(line_list[0].strip())
            value = filter_brackets(line_list[1].strip())
            fdict[key] = value

    return fdict

def run_comparation(golden_dict, sample_dict):
    in_golden_set = set(golden_dict.items())-set(sample_dict.items())
    in_sample_set = set(sample_dict.items())-set(golden_dict.items())

    in_golden_dict = change_binaryTupleSet_to_dict(in_golden_set)
    in_sample_dict = change_binaryTupleSet_to_dict(in_sample_set)

    return generate_diff_dict(in_golden_dict, in_sample_dict)

def generate_diff_dict(gdt, sdt):
    diff_dict = {}
    diff_value = []
    not_in_golden = []
    not_in_sample = []

    for gkey in gdt:
        if not sdt.has_key(gkey):
            dt = {}
            #dt['info'] = 'Info exists in Golden but not in Sample.'
            dt['key'] = gkey
            dt['value'] = gdt[gkey]
            not_in_sample.append(dt)
        else:
            dt = {}
            #dt['info'] = 'different value.'
            dt['key'] = gkey
            dt['golden_value'] = gdt[gkey]
            dt['sample_value'] = sdt[gkey]
            diff_value.append(dt)

    for skey in sdt:
        if not gdt.has_key(skey):
            dt = {}
            #dt['info'] = 'Info exists in Sample but not in Golden.'
            dt['key'] = skey
            dt['value'] = sdt[skey]
            not_in_golden.append(dt)

    diff_dict['diff_value'] = diff_value
    diff_dict['not_in_golden'] = not_in_golden
    diff_dict['not_in_sample'] = not_in_sample

    return diff_dict

def change_binaryTupleSet_to_dict(btset):
    dt = {}
    for item in btset:
        key = item[0]
        value = item[1]
        dt[key] = value

    return dt

def is_fai_pass(diff):
    list0 = diff['diff_value']
    list1 = diff['not_in_sample']
    list2 = diff['not_in_golden']

    if list0 or list1 or list2:
        return False
    else:
        return True

def generate_out_put_string(diff, string, lang='cn'):
    list0 = diff['diff_value']
    list1 = diff['not_in_sample']
    list2 = diff['not_in_golden']

    if list0:
        string += '  %s\n' % INFO_DIFFERENT_VALUE
        for info in list0:
            string += '    key: [%s]\n' % info['key']
            string += '      golden_value: [%s]\n' % info['golden_value']
            string += '      sample_value: [%s]\n' % info['sample_value']

    if list1:
        string += '\n  %s\n' % INFO_NOT_IN_GOLDEN
        for info in list1:
            string += '    [%s]: [%s]\n' % (info['key'], info['value'])

    if list2:
        string += '\n  %s\n' % INFO_NOT_IN_SAMPLE
        for info in list2:
            string += '    [%s]: [%s]\n' % (info['key'], info['value'])

    return string

def output_diff_to_file(diff, file):
    result_string = '%s: ' % INFO_FAI_RESULT
    r0 = is_fai_pass(diff['sysprop'])
    r1 = is_fai_pass(diff['settings'])
    r2 = is_fai_pass(diff['ringtone'])

    if r0 and r1 and r2:
        is_pass = 'PASS'
        result_string += 'PASS'

    else:
        is_pass = 'FAIL'
        result_string += 'FAIL'

        if not r0:
            result_string += '\n\n[%s]\n' % INFO_SYSPROP_DIFF
            result_string = generate_out_put_string(diff['sysprop'], result_string)
        if not r1:
            result_string += '\n\n[%s]\n' % INFO_SETTINGS_DIFF
            result_string = generate_out_put_string(diff['settings'], result_string)
        if not r2:
            result_string += '\n\n[%s]\n' % INFO_RINGTONE_DIFF
            result_string = generate_out_put_string(diff['ringtone'], result_string)

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    f = open(file, 'wb')
    result = str(result_string)
    f.write(result)
    f.close()

    show('%s: %s' % (INFO_FAI_RESULT, is_pass))
    show(HINT_RESULT_OUTPUT_SUCCESS % file)

def show(msg):
    type= sys.getfilesystemencoding()
    #change string to system encoding for messy code
    result = msg.decode('utf-8').encode(type)
    print result

def write(msg):
    type= sys.getfilesystemencoding()
    #change string to system encoding for messy code
    result = msg.decode('utf-8').encode(type)
    raw_input(result)