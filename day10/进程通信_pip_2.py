#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#父进程发数据给子线程
from multiprocessing import Process, Pipe

#子进程发数据给父进程

def f(conn):
    print("from parent:",conn.recv())  #接受父进程的数据
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  #生成一个管道实例
    p = Process(target=f, args=(child_conn,))
    p.start()
    parent_conn.send("hello from parent_conn...") #将数据发给子线程
    p.join()