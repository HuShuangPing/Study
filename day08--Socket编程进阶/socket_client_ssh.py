#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing
import socket

client =socket.socket()
client.connect(('localhost',9999))


while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode())
    cmd_res_size = client.recv(1024)   #接受从服务端发送的数据大小
    print("命令结果大小：",cmd_res_size)
    received_size = 0
    received_data = b''
    #循环接受，次数是从服务端发过来的命令结果大小
    while received_size < int(cmd_res_size.decode()):   #收到的数据大小不等于实际要发送的总数据即cmd_res_size大小，就要继续接受数据
        data = client.recv(1024)
        received_size +=len(data)   #将接受数据大小进行累加
                         #用处：每次收到的数据可能小于1024，必须用len()进行判断
        #print(data.decode())
        received_data += data
    else:
        print("cmd res receive done...",received_size)
        print(received_data.decode())
    # cmd_res = client.recv(1024)
    #
    # print(cmd_res.decode())