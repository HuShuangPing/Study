#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import paramiko
# 创建SSH对象
ssh = paramiko.SSHClient()  #一个客户端
# 允许连接不在know_hosts文件中的主机

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.0.0.31', port=52113, username='root', password='123456')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
#第一个参数是标准输入，即你输入的数据
#第二个参数是标准输出，即客户端输出结果
#第三个参数是命令执行中产生的错误

# 获取命令结果
res,err = stdout.read(),stderr.read()
result = res if res else err

print(result.decode())

# 关闭连接
ssh.close()