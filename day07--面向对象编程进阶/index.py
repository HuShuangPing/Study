#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

from lib.aa import C

obj = C()
print(obj.__module__)  # 输出 lib.aa，即：输出模块
print(obj.__class__ )     # 输出 lib.aa.C，即：输出类