FAI Compare
==============

手机和Golden Simple手机的信息比较, 生成异常信息报告.

目前比较的信息包括:

system property
settings
ringtones

从golden phone中pull信息
python fai -p path
    其中path表示存放golden info的位置

获取sample phone和golden的比较信息
python fai -c path
    其中path表示存放golden info的位置

输出文件
out/compare_result.txt

