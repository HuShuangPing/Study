#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#3.嵌套函数
'''
   定义：在函数内声明一个函数
'''

def foo():
    print("in the foo")
    def bar():        #局部变量，在局部内定义，在局部内使用
        print("in the bar")
    bar()

foo()

