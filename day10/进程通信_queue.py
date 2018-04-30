#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


from multiprocessing import Process, Queue  #进程Queue

# def f(q):
#     q.put([42, None, 'hello'])

def f(qq):
    print("in child:",qq.qsize())
    qq.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))  #把q传给创建的进程q，即把父进程的q传给创建的子线程
                                      #相当于是clone一份
    p.start()
    print(q.get())  #print([42, None, 'hello'])
    p.join()
