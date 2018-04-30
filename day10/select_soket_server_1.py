#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import select
import socket
import queue

#Windows下不支持epoll，支持select

server = socket.socket()
server.bind(('localhost',9000))
server.listen(1000)

#在非阻塞的情况下实现单线程I/O多路复用
server.setblocking(False) #不阻塞



inputs = [server,]   #存放监测的链接
                     #监测自己
outputs = []


readable,writeable,exceptional =  select.select(inputs,outputs,inputs) #括号里第一个参数是你想让内核监测的链接
                                                                       #第二个参数是
                                                                       #第三个参数存放链接断的
print(readable,writeable,exceptional)

for i in readable:
        conn,addr = server.accept()   #没有链接会报错
        print(conn,addr)
        inputs.append(conn)
        #是因为这个新建立的连接还没发数据过来，现在就接收的话程序就报错了，
         #所以要想实现这个客户端发数据来时server端能知道，就需要让select再监测这个conn

        #现在列表中有input[server,conn]现在进行只要有一个活动就会返回
        #此时在readable中可能是server也可能是conn
        #如果返回的是server，就会认为来了新的链接,返回的是conn就会接受数据