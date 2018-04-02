#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import sys,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #获取本程序的父文件的父文件的路径，即Atm

sys.path.append(BASE_DIR)   #添加到环境变量

from day05 import package_test
package_test.test1.test()