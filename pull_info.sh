#!/bin/sh
#pull_info.sh

#ying.tan@tcl.com

adb install utils/goldencollector.apk

adb shell am start -n com.tcl.goldencollector/.MainActivity
adb pull /sdcard/golden_collection.txt ./bin
adb shell rm -f /sdcard/golden_collection.txt

adb uninstall com.tcl.goldencollector
adb shell rm -f /data/local/tmp/goldencollector.apk
