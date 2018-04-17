#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):    #和客户端所有的交互都是在handle中写的
        while True:      #多次发送数据
            try:
                self.data = self.request.recv(1024).strip()  #第一步重写handler()方法
                                                            #每次传送的数据的实例就是self
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err",e)
                break
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.ForkingThreadingTCPServer((HOST, PORT), MyTCPHandler)  #支持多线程，每来一次开辟新的进程
           #ForkingThreadTCPSSever在Linux中可可以创建多线程
    server.serve_forever()