#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#在Windows中引用进程池，需导入freeze_suport
from  multiprocessing import Process, Pool,freeze_support   #导入Pool
import time
import os

def Foo(i):
    time.sleep(2)
    print("in process",os.getpgid())
    return i + 100

def Bar(arg):
    print('-->exec done:', arg,os.getpgid())

if __name__=='__main__':   #为了区分主动你是手动执行这个脚本还是从别的地方当做一个模块去调用
                           #如果你是手动执行这个脚本，下面的代码就会执行
                           #如果你是从别的地方调用，就不会执行下面的代码
    freeze_support()   #在Windows上引用进程池需要做的操作
    pool = Pool(processes=5)  #允许进程池中同时放入5个进程
    print("主进程：",os.getpgid())  #测试Bar是主进程调用的
    for i in range(10):
            pool.apply_async(func=Foo, args=(i,), callback=Bar) #5个进程并行执行
                                                                #主进程调用：callback=回调  执行完Foo,就执行Bar
            #pool.apply(func=Foo, args=(i,)) #5个进程串行执行
    print('end')
    pool.close()
    pool.join() #进程池中进程执行完毕后再关闭，
                # 如果注释，那么程序直接关闭。.join()