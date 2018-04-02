#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#模块

#定义：
#用来从逻辑上组织Python代码（变量，函数，类，罗：实现一个功能），本质是Python文件
#（文件名：test.py对应的模块名:test

#包 定义：从逻辑上组织模块
# 本质就是一个目录(必须带有__init__.py文件)



#导入
#import module_name,module2_name
#from module_1 import * 导入模块中所有的元素，不建议使用
#from module_1 import test1 as t1
#from module_1 import test1,test2,test3


#import本质
#导入模块的本质就是把Python文件解释一遍
  ##import module_name --->module_name.py-->module_name.py的路径---》sys.path

#导入包的本质就是执行该包下__init__.py文件

#模块分类：
'''
a.标准库
    a.1 时间模块：time和datetime
        时间戳：1970到现在的秒数
        格式化字符串：按照自己定义的
        元组(struct_time):共九个元素
    a.2 random模块
    a.3 os模块
    a.4 sys模块
    a.5 shutil模块
    a.6 json和pickle
    a.7 shelve模块
    a.8 xml模块
b.开源模块
c.自定义模块
'''









