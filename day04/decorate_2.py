#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

# 2.高阶函数
'''
   a.把一个函数名当做实参传给另外一个函数
       (在不修改被装饰函数源代码的情况下为其添加功能)
   b.返回值中包含函数名
      （不修改函数的调用方式）
'''

import time

# a.把一个函数名当做实参传给另外一个函数
# def bar():
#     time.sleep(3)
#     print("in the bar")
#
# def test1(func):
#     start_time = time.time()
#     func()   #run bar
#     stop_time = time.time()
#     print('the func run time is %s'%(stop_time-start_time))
#
# test1(bar)

# b.返回值中包含函数名

def bar():
    time.sleep(3)
    print("in the bar")

def test2(func):
    print(func)
    return func

#print(test2(bar))   #打印结果为：
                            # <function bar at 0x02228F18>
                            # <function bar at 0x02228F18>
#t=test2(bar)
#print(t)       #打印结果为：
                    # <function bar at 0x02228F18>
                    # <function bar at 0x02228F18>
#t()             #输出结果为：
                    # <function bar at 0x02138F18>
                    # in the bar
bar = test2(bar)
bar()             #输出结果为：
                        # <function bar at 0x00798F18>
                        # in the bar
#------bar此时相当于加了一个新功能