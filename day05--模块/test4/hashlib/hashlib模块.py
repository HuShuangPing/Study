#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#hashlib  用于加密相关的操作

import hashlib

#md5()加密
m = hashlib.md5()       #md5不能反解
m.update(b"Hello")
print(m.hexdigest())    #输出时是十六进制加密的

m.update(b"It's me")   #这段密文是对"Hello"+"It's  me"的加密
print(m.hexdigest())

m.update(b"It's long time we...")
print(m.hexdigest())

#sha1()加密

s2 = hashlib.sha1()
s2.update(b"HelloIt'me".encode(encoding="utf-8"))
print(s2.hexdigest())

#hmac模块加密
#它内部对我们创建 key 和 内容 再进行处理然后再加密
import hmac

h = hmac.new(b"12345","250".encode(encoding="utf-8"))
print(h.hexdigest())
print(h.digest())    #十进制