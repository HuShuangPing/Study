#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#把子线程变成守护线程
  #守护线程是为非守护线程服务的，可以管理文件，接口，回收资源
  #非守护线程不会等待守护线程，会直接往下走
import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)


start_time = time.time()
t_objs = []   #存线程实例
for i in range(50):
    t = threading.Thread(target=run,args=("t%s"%i,))
    t.setDaemon(True)   #把当前线程设置为守护线程，必须在start之前设置
    t.start()
    t_objs.append(t) #为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

# for t in t_objs:
#     t.join()

print("cost:",time.time()-start_time)  #主线程是非守护线程，主线程执行完毕就直接退出程序