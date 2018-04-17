#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import socket
import os


server = socket.socket()
server.bind(('localhost',9999))
server.listen()

while True:
    conn,addr = server.accept()
    print("new conn",addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令",data)
        cmd_res = os.popen(data.decode()).read()
           #os.popen用于从一个命令打开一个管道
           #os.popen()参数是字符串，
           # 接受的数据是从客户端发来的ASCII码类型的
           # 因此要进行解码
        print("before send...",len(cmd_res))

        if len(cmd_res) == 0:
            cmd_res = "cmd has out output"
        conn.send(str(len(cmd_res.encode("utf-8"))).encode("utf-8"))  #先发送大小给客户端
                         #中文需要进行转码，1个中文占3个位

        conn.send(cmd_res.encode("utf-8"))
        print("after send...")
        #send()发送比特流，要对字符串进行编码




#问：客户端不知道自己要接受多少次数，
#    而服务端也不知道自己要发送多少次数据，怎么办？
# 答：现在服务端对要发送数据的长度进行判断，然后发送给客户端