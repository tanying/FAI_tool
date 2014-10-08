FAI Compare
==============

手机和Golden Simple手机的信息比较, 生成异常信息报告.
环境要求: python2.*

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

若window没有预装python, 需要安装python.
python文件的安装包在py文件夹下.

windows安装方法:
1.安装python
  启动命令行工具
  cd FAI_tool
  install.bat(此脚本会判断当前系统是32位还是64位,从而选择安装对应python)
  点下一步直到安装结束
2.添加环境变量
  右击我的电脑, 点选"属性", 打开系统属性窗口
  选择"高级"标签页, 点击"环境变量"按钮
  在系统变量中找到"path", 点击编辑按钮
  在变量值最后追加"C:\Python27"(默认安装路径)
  点确定, 重新打开命令行工具

