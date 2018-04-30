#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import select
import socket
import queue


server = socket.socket()
server.bind(('localhost',9000))
server.listen(1000)

#在非阻塞的情况下实现单线程I/O多路复用
server.setblocking(False) #不阻塞



inputs = [server,]   #存放监测的链接
                     #监测自己
outputs = []

while True:  #让新来的链接进行检测
    readable,writeable,exceptional =  select.select(inputs,outputs,inputs)
    print(readable,writeable,exceptional)

    for r in readable:
        if r is server:   #代表来了一个新的链接
            conn,addr = server.accept()
            print("来了一个新链接",addr)
            inputs.append(conn)
        else:
            data = r.recv(1024)   #让新来的链接收数据
            print("收到数据",data)
            r.send(data)   #将数据返回
                            #但是不行，因为不知道客户端收不收,数据会丢失
            print("send done...")