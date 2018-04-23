#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import time
import threading

#通过设置标志位，实现两个线程的交互
    #evet.set()设置标志位
    #event.wait() 等待标志位设置
    #event.clear() 将标志位清空
    #event.isset() 判断标志位是否被设定

event = threading.Event()   #生成event对象
def lighter():
    count = 0
    event.set()
    while True:
        if count>5 and count<10:   #改成红灯
            event.clear()  #把标志位清了
            print("变成红灯")
        elif count>10:
            event.set()    #变成绿灯
            print("变成绿灯")
            count=0
        else:
            print("变成绿灯")
        time.sleep(1)
        count+=1

def car(name):
    while True:
        if event.is_set():   #有标志位代表绿灯
          print("[%s] running..."%name)
        else:
            print("[%s] sees red light,waithing..."%name)
            event.wait()   #等待标志位设置
            print("[%s] green light is on,starting running..."%name)

light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car,args=("Tesla",))
car1.start()