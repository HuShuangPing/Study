#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


#夸包执行文件

#使用相对路径

print(__file__)   #返回当前程序的相对路径

#把相对路径添加系统环境变量中，会找不到这个程序
#因此要获取程序绝对路径，动态加载到环境变量中

import os
import sys
print(os.path.abspath(__file__))   #获取绝对路径

#dirname获取路径名，不要路径名，即去掉本程序的文件名
print(os.path.dirname(os.path.abspath(__file__)))   #获取到本程序的父文件路径

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #获取本程序的父文件的父文件的路径，即Atm

sys.path.append(BASE_DIR)   #添加到环境变量中


from cnf import settings
from core import main

main.login()


