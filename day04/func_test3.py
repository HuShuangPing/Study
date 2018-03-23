#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#默认参数
def test1(x,y=2):
    print(x)
    print(y)

#默认参数是创建函数时进行初始化的参数

#默认参数是可以进行重新赋值的
test1(1,2)

#参数组
 #实参是动态的，形参使用参数组

def test2(*args):
    print(args)
test2(*[1,2,3,4,5])  # args = tuple([1,2,3,4]) 元组

def test3(x,*args):
    print(x)
    print(args)

test2(1,2,3,4,5)  #打印的结果是1,(2,3,4,5)


#接受字典参数
def test3(**kwargs):
    print(kwargs)
    print(kwargs["name"])  #访问字典中的value值

test3(name="alex",age=20,sex="man")

