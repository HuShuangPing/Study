#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
#
# f = Foo("alex")
# print(type(f))    #类型是Foo
# print(type(Foo))  #打印的类型是type


def func(self):
    print('hello %s' %self.name)
def __init__(self,name,age):
    self.name = name
    self.age = age

Foo = type('Foo', (object,), {'talk': func,
                       '__init__':__init__})
    #构造Foo对象，而这个类就是Foo类
    #(object,)是继承类，加逗号默认是元组，不加会被认为是一个值
    # 可以不写，但必须要有()
    # '__init__':__init__  关联构造方法
f = Foo("Chrn",22)
f.talk()
print(type(Foo))   #打印输出：type

## type是类的类