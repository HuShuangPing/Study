#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import threading
import time

#注在Python3上不不需要加锁的

def run(n):
    lock.acquire()    #获取一把锁
    global  num
    num +=1
    time.sleep(1)  #尽量不要使用sleepk
    lock.release()  #释放锁
                    #此时程序串行执行

lock = threading.Lock()  #创建锁的一个实例
num = 0
t_objs = [] #存线程实例
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s" %i ,))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print("----------all threads has finished...",threading.current_thread(),threading.active_count())

print("num:",num)