#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import select
import socket
import queue

#通过队列让数据从服务器等一段时间发送给客户端
server = socket.socket()
server.bind(('localhost',9000))
server.listen(1000)

#在非阻塞的情况下实现单线程I/O多路复用
server.setblocking(False) #不阻塞

msg_dic = {}

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
            #将新建链接里放到队列中
            msg_dic[conn] = queue.Queue() #初始化一个队列，后面的队列要返回给客户端的数据
        else:
            data = r.recv(1024)   #让新来的链接收数据
            print("收到数据",data)
            msg_dic[r].put(data)
            outputs.append(r)   #放入返回的链接队列里
    for w in writeable:  #要返回给客户端的链接列表
                         #在下次select之前把数据发送
        data_to_client = msg_dic[w].get()
        w.send(data_to_client)

        outputs.remove(w)  #确保下次训话的时候writeable，不返回这个已经发送的链接
    #处理异常
    for e in exceptional:  #此时链接断了，无需检测
                           #把链接实例从input,output中除去
          if e in outputs:
              outputs.remove(e)
          inputs.remove(e)

          del msg_dic[e]