#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#等待子线程运行结束
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThread,self).__init__()   #重构父类方法
        self.n = n
        self.sleep_time = sleep_time
    def run(self):   #必须写成run
        print("running task",self.n)
        time.sleep(self.sleep_time)
        print("task done",self.n)

t1 = MyThread("t1",2)
t2 = MyThread("t2",4)  #此时t1的sleep时间与t2不同

t1.start()
t2.start()
t1.join()   #等待t1子线程执行结果，t1没有执行完，程序不往下面执行
t2.join()   #等待t2
print("main thread....")#输出结果:
                          #task done t1
                          #task done t2
                          #main thread....
