#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#模块
'''
import sys
#print(sys.path)   #打印出的是环境变量
print(sys.argv)'''

import os
cmd_res =os.system("dir")   #执行命令，不保存结果
print(cmd_res)