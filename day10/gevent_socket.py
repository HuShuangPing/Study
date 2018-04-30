#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#实现并发
import sys
import socket
import time
import gevent

from gevent import socket, monkey

monkey.patch_all()


def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))  #绑定端口
    s.listen(500)
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli)  #启动一个协程
                                           #把生成的客户端实例，交给handle_request处理

def handle_request(conn):
    try:
        while True:
            data = conn.recv(1024)
            print("recv:", data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)  #把客户端关闭

    except Exception as  ex:
        print(ex)
    finally:
        conn.close()


if __name__ == '__main__':
    server(8001)  #启动8001端口