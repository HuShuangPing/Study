#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


import module_1
from module_1 import *   #引入模块所有的元素
from module_1 import test1 as t1
from module_1 import test1,test2,test3
from module_1 import name


print(module_1.name)   #import 导入模块
module_1.sayhi()
t1()                  #from导入模块
print(name)