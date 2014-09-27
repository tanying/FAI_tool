FAI
==============

手机和Golden Simple手机的信息比较, 生成异常信息报告.

目前比较的信息包括:

system property
settings
contacts
ringtones
notifications
alarms

启动比较
python ginfocmp

输出文件
out/report.txt

考虑工厂机器没有安装adb的情况
sudo apt-get install android-tools-adb

sudo adb kill-server
sudo adb start-server


