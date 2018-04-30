#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#在屏幕中输出数据时，不会乱
from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()  #获得锁
    try:
       print('hello world', i)
    finally:
        l.release()   #释放锁


if __name__ == '__main__':
    lock = Lock()   #生成一个锁的实例

    for num in range(100):
        Process(target=f, args=(lock, num)).start()  #把锁传给进程