# -*- coding: utf8 -*-

__author__ = 'Tan Ying<ying.tan@tcl.com>' 

import os
import sys
import log
import json
import config
import commands

logger = log.getLogging('utils.py')

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

def pull_by_apk(cfile):

    if is_pull_aready('golden_collection.flag'):
        os.system('adb pull /sdcard/golden_collection.txt ./%s' % cfile)
        os.system('adb uninstall com.tcl.goldencollector')
        os.system('adb shell rm -f /data/local/tmp/goldencollector.apk')
        os.system('adb shell rm -f /sdcard/golden_collection.flag')
        os.system('adb shell rm -f /sdcard/golden_collection.txt')
    else:
        pull_by_apk(cfile)

def pull_info_from_phone(is_golden):
    global PULL_SUCCESS_FLAG

    if is_golden:
        property_file = GOLDEN_PROPERTY
        collection_file = GOLDEN_COLLECTION
        unconnected_hint = 'Please connect the Golden Phone with PC by USB.'
        success_hint = 'Pull properties from golden phone successful.\n'
    else:
        property_file = SAMPLE_PROPERTY
        collection_file = SAMPLE_COLLECTION
        unconnected_hint = 'Please connect the Sample Phone with PC by USB for comparation.'
        success_hint = 'Pull properties from sample phone successful.\n'

    command = 'adb shell getprop > %s' % property_file
    status, output = commands.getstatusoutput(command)

    if status == 0:
        os.system('adb install utils/goldencollector.apk')
        os.system('adb shell am start -n com.tcl.goldencollector/.MainActivity')

        pull_by_apk(collection_file)

        PULL_SUCCESS_FLAG = True
        print success_hint
    else:
        print unconnected_hint
        #restart server
        os.system('sudo adb kill-server')
        os.system('sudo adb start-server')

        usb_connected = raw_input('enter(aleady), else(exit)')

        if usb_connected == '':
            pull_info_from_phone(is_golden)
        else:
            print 'You pressed any key to exit, bye!'
            sys.exit(1)



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

def generate_out_put_string(diff, string):
    list0 = diff['diff_value']
    list1 = diff['not_in_sample']
    list2 = diff['not_in_golden']

    if list0:
        string += '  Golden Phone and Sample Phone have different value.\n'
        for info in list0:
            string += '    key: %s\n' % info['key']
            string += '      golden_value: %s\n' % info['golden_value']
            string += '      sample_value: %s\n' % info['sample_value']

    if list1:
        string += '\n  Info exists in Golden but not in Sample.\n'
        for info in list1:
            string += '    [%s]: [%s]\n' % (info['key'], info['value'])

    if list2:
        string += '\n  Info exists in Sample but not in Golden.\n'
        for info in list2:
            string += '    [%s]: [%s]\n' % (info['key'], info['value'])

    return string

def output_diff_to_file(diff, file):
    result_string = 'FAI result: '

    r0 = is_fai_pass(diff['sysprop'])
    r1 = is_fai_pass(diff['settings'])
    r2 = is_fai_pass(diff['ringtone'])

    if r0 and r1 and r2:
        is_pass = 'PASS'
        result_string += 'PASS'

    else:
        is_pass = 'FAIL'
        result_string += 'FAIL\n\n'


        if not r0:
            result_string += '[system property difference]\n'
            result_string = generate_out_put_string(diff['sysprop'], result_string)
        if not r1:
            result_string += '[settings difference]\n'
            result_string = generate_out_put_string(diff['settings'], result_string)
        if not r2:
            result_string += '[ringtone difference]\n'
            result_string = generate_out_put_string(diff['ringtone'], result_string)

    f = open(file, 'wb')
    result = str(result_string)
    f.write(result)
    f.close()

    print 'FAI RESULT: %s' % is_pass
    print 'The detail report have output successfully in [%s]' % file

def parse_collection_txt(file):
    fdict = {}

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

    fdict['settings'] = sdict
    fdict['ringtone'] = rdict
    return fdict