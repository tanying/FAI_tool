FAI Compare
==============

手机和Golden Simple手机的信息比较, 生成异常信息报告.

目前比较的信息包括:

system property
settings
ringtones

启动比较
python fai

输出文件
out/compare_result.txt

问题: 工具是否需要面向工厂？工厂机器是何环境？
1.若为linux

    工厂机器可能没有安装adb
    需要sudo apt-get install android-tools-adb
    之后启动server的操作需要root密码

2.若为windows
    需预装python2.*
    需配置环境变量    
    需安装adb
    需添加中文乱码处理

3.手机有可能没有开启usb调试
    有没有adb命令默认把usb调试打开