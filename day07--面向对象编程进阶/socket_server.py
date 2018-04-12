#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#服务器端

import socket
server = socket.socket()
server.bind(('localhost',6969)) #绑定要监听端口
server.listen(5) #监听

print("我要开始等电话了")

conn,addr = server.accept()  #等待电话打进来
    #返回两个值，第一个值是:conn链接标志位，即客户端发过来的在服务器端生成的实例
    #            第二个值是：对方的地址

print("电话来了")

#data = server.recv(1024)  #接受消息
                  #并发，出现错误
#应改成
data = conn.recv(1024)

print("recv:",data)
conn.send(data.upper)  #发送消息
server.close()           #关闭






