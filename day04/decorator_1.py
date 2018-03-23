#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#1.函数即“变量”
'''
  def test():
    pass
相当于test = "函数体"
'''


#def foo():
#    print("in the foo")
#    bar()
#def bar():
#    print("in the bar")     #问1：为什么bar函数在foo下面定义不报错
#
#foo()               #答：调用foo时bar已定义

def foo():
    print("in the foo")
    bar()

foo()           #问2：放在两个函数之间调用foo出现错误
                #答：调用foo时bar还没有定义
def bar():
    print("in the bar")
