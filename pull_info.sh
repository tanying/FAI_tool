#!/bin/sh
#pull_info.sh

#ying.tan@tcl.com

binPath="bin/"

is_pull_aready(){
res=$(adb shell ls /sdcard/ | grep golden_collection.flag)
echo $res
if [ $res=="golden_collection.flag" ];then
adb pull /sdcard/golden_collection.txt collection_golden.txt
adb shell getprop > property_golden.txt
adb uninstall com.tcl.goldencollector
adb shell rm -f /sdcard/golden_collection.txt
adb shell rm -f /sdcard/golden_collection.flag
adb shell rm -f /data/local/tmp/goldencollector.apk
else
is_pull_aready
fi
}

if [ ! -d "$binPath" ];then
mkdir $binPath -m 777
fi

cd $binPath
adb install ../utils/goldencollector.apk
adb shell am start -n com.tcl.goldencollector/.MainActivity
is_pull_aready
cd ..





