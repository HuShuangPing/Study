#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#输入的信息设置为密文
import getpass

_username = "Alex"
_password = "123"

#产生密文
#username = getpass.getpass(input("username:"))
#password = getpass.getpass(input("password:"))

#判断密码正确性
username = input("username:")
password = input("password:")
if _username==username and _password==password:
    print("Welcome user {name}".format(name=username))
else:
    print("Invaild usernam or password")

#在Python中若定义的变量是int类型，超过了int类型，会自动转化为float类型
# 数据类型：
# 1.数字
#   int（整数），float（浮点）数   复数 a+bj
#2.布尔值（真或假）
#3.bytes类型
  #在Python3中二进制数据（如：视频）用bytes类型表示
  #二进制与字符类型必须分开
  #即字节包中无法搜索字符串，反之同理
  #在soket 网络编程（数据传送）必须使用二进制形式
msg = "我爱北京天安门"
print(msg.encode(encoding="utf-8"))   #字符转换为二进制
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))  #二进制转换为字符

#三元运算
a,b,c = 1,3,5
if a>b:d=a
else:d=c

#进制
#二进制   前缀是0b
#八进制   前缀是0o
#十六进制 前缀是0x

