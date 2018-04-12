#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing
import socket

server = socket.socket()

server.bind(('localhost',6969))
server.listen(5)   #数字5表示最多允许5个排队

while True:
    conn, addr = server.accept()  # 等电话打进来
    print(conn, addr)
    print("电话来了")
    count = 0
    while True:    #使客户端断开了，服务器可以处于等待状态
        data = conn.recv(1024)
        print("recv:",data)
        if not data:     #发送数据为空，此次数据的接受断开
            print("client has lost...")
            break
        conn.send(data.upper())
        count+=1
        if count >10:break

server.close()
