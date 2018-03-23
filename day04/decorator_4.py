#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#书写装饰器

import time
#定义一个高阶函数
def timer(func):      #相当于test1=timer(test1)
    def deco(*args,**kwargs):    #若调用的函数有参数则传入，无就不传入
        start_time=time.time()
        func(*args,*kwargs)
        stop_time = time.time()
        print("the func run time is %s"%(stop_time-start_time))
    return deco

@timer
def test1():
    time.sleep(3)
    print("in the test1")
@timer
def test2(name,age):
    time.sleep(3)
    print("in the test2")

# deco(test1)   #注：加括号会把test1运行结果传给deco函数
# #此时在改函数的调用方式，问：在不修改函数调用方式怎么添加功能
# #答：此时需要将高阶函数添加返回值
# test1 = deco(test1)

#将嵌套函数引入高阶函数:定义一个timmer函数

#print( timmer(test1))  #返回的是deco的内存地址值

#test1 = timmer(test1)  #func=test1
test1()
test2("Jack",22)