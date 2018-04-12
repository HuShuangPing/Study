#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#夸包引入模块

import sys,os

print(sys.path)   #环境变量路径，列表

#dirname获取路径名，不要路径名，即去掉本程序的文件名
print(os.path.dirname(os.path.abspath(__file__)))   #获取到本程序的父文件路径

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #获取本程序的父文件的父文件的路径，即Atm

sys.path.append(BASE_DIR)   #添加到环境变量

import module_1
module_1.sayhi()   #import导入整个代码
