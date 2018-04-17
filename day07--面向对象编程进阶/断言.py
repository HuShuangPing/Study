#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


import importlib
aa = importlib.import_module("lib.aa")  #导入的是aa
obj = aa.C()
print(obj.name)  #效果与上面相同

assert type(obj.name) is str   #assert断言
                               #断言正确就往下走，不正确就报错
                      #若后面的程序很重要，依赖前面的程序，就采用断言
print("ddd")