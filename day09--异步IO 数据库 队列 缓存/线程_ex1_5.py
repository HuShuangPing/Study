#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


#计算启动50线程循环所花费的时间
     # 在线程_ex1_3基础上加个for循环

import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)


start_time = time.time()
t_objs = []   #存线程实例
for i in range(50):
    t = threading.Thread(target=run,args=("t%s"%i,))
    t.start()
    t_objs.append(t) #为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

for t in t_objs:
    t.join()

print("cost:",time.time()-start_time)