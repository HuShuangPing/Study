#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

from multiprocessing import Process, Pipe

#子进程发数据给父进程

def f(conn):
    conn.send([42, None, 'hello from child1'])
    conn.send([42, None, 'hello from child2'])
    conn.send([42, None, 'hello from child3'])   #子进程多次发数据给父进程
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  #生成一个管道实例
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    print(parent_conn.recv())
    print(parent_conn.recv())  #父进程多次接受子线程发来的数据
    p.join()