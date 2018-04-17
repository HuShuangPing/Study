#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

# mode = __import__("lib.aa") #其实导入的是lib
# obj = mode.aa.C()
# print(obj.name)


#官方建议
import importlib
aa = importlib.import_module("lib.aa")  #导入的是aa
obj = aa.C()
print(obj.name)  #效果与上面相同