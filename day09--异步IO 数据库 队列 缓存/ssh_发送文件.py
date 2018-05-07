#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

 
import paramiko

#基于用户名和密码的 transport 方式登录
#基于用户名和密码的 sshclient 方式登录是传统的连接服务器、执行命令、关闭的一个操作，
#有时候需要登录上服务器执行多个操作，比如执行命令、上传/下载文件，则基于用户名和密码的 sshclient 方式无法实现

transport = paramiko.Transport(('10.0.0.31', 52113))
transport.connect(username='root', password='123456')  #建立链接


sftp = paramiko.SFTPClient.from_transport(transport) #将链接传给SFTPClient

# 将location.py 上传至服务器 /tmp/test.py
#sftp.put('笔记', '/tmp/test_from_win')


# 将remove_path 下载到本地 local_path
sftp.get('/root/oldgirl.txt', 'fromlinux.txt')

transport.close()
