#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


import socket
client = socket.socket()

#client.connect(('192.168.16.200',9999))
client.connect(('localhost',9999))

class FtpClient(object):
    def __init__(self):
        pass
    def help(self):   #打印指令的信息
        msg = '''
        ls
        pwd
        cd ../..
        get filename
        put filename
        '''
    def connect(self,ip,port):
        self.client.connect('localhost',9999)


    def interaction(self):
        while True:
            cmd = input(">>").strip()
            if len(cmd) == 0: continue
            cmd_str = cmd.split()[0]
            if hasattr(self,"cmd %s" % cmd_str):
                func = getattr(self,"cmd %s " %cmd_str)
                func(cmd)
    def put(self):
        pass
    def get(self):
        pass
