#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#一次启动多个线程
  #循环

import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)


start_time = time.time()

for i in range(50):
    t = threading.Thread(target=run,args=("t%s"%i,))
    t.start()

print("cost:",time.time()-start_time)   #计算循环启动50个线程的所需时间
                        #输出结果cost: 0.019001007080078125不是两秒
                        #主线程启动子线程，子线程就是独立的了，主线程和子线程是并行的
                        #但程序在退出前会等待所有线程执行完毕后再退出程序
                        #主线程就是程序本身