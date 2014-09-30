FAI Compare
==============

手机和Golden Simple手机的信息比较, 生成异常信息报告.

目前比较的信息包括:

system property
settings
ringtones

从golden phone中pull信息
python fai -p path(可选)
    其中path表示存放golden info的位置
    如果没有输入path会将info存放在当前路径的bin目录下

获取sample phone和golden的比较信息
python fai -c path(可选)
    其中path表示存放golden info的位置
    如果没有输入path会将info存放在当前路径的bin目录下
   
输出文件
out/compare_result.txt

