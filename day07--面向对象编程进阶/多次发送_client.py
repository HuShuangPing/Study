#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing
import socket

client = socket.socket()

client.connect(('localhost',6969))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
    client.send(msg.encode("utf-8"))  #不能发送空消息，会卡住
    data = client.recv(10240)
    print("recv:",data.decode())

client.close()