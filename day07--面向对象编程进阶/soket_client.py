#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#客户端
import socket

client = socket.socket() #声明socket类型，同时生成socket连接对象

client.connect(('localhost',6969))

#client.send(b"Hello World")  #发送信息
                            #在Python只发送bytes类型，即比特流
#发中文
client.send("我爱祖国".encode("utf-8"))
#bytes类型只能接受ASCII码的数据类型
#先进行encode()，转成ASCII码支持的类型


data = client.recv(1024)        #接受信息
                                #参数为接受的字节数，即1K

print("recv: ",data.decode())
#将ASCII码支持的类型进行解码，才能看懂接受的数据



client.close()               #关闭

