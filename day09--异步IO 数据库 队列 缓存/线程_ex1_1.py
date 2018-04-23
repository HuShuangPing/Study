#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


#启动线程方式1
import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)

t1 = threading.Thread(target=run,args=("t1",))
t2 = threading.Thread(target=run,args=("t2",))   #在args中加入逗号，不然会认为是元组
t1.start()
t2.start()   #一共等了2秒钟