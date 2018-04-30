#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


#默认用epoll

import selectors
import socket


sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr,mask)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)
    #第一个参数将
    #新连接注册read回调函数


def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 9999))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)
#第一个参数是将新建的sock实例让sel监听
#第三个参数是只要来了新的链接，就调用accept函数

while True:
    events = sel.select() #默认阻塞，有活动连接就返回活动的连接列表
    for key, mask in events:
        callback = key.data #相当于调用accept
        callback(key.fileobj, mask) #key.fileobj=  文件句柄