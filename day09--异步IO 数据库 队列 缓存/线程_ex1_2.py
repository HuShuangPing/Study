#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#启动线程方式2：以类的方式

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()   #重构父类方法
        self.n = n
    def run(self):   #必须写成run
        print("running task",self.n)

t1 = MyThread("t1")
t2 = MyThread("t2")