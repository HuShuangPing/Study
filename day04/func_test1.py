#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#面对对象：类  》》class
#面向过程：过程》》def
#函数式编程：函数》》def

#定义一个函数
def func1():
    '''testing'''
    print("in the func1")
    return 0   #返回值：返回一个值并结束该函数
               #返回值中可以包括多个返回值

#定义一个过程,没有返回值的函数
def func2():
    '''testing'''
    print("in the func2")

#调用
x=func1()
y=func2()

print("from func1 return is %s"%x)    #根据函数返回一个0
print("from func2 return is %s"%y)    #没有返回值Python会返回None