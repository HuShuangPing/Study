#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

s= "你好"
s_gbk=s.encode("gbk")    #此时编码是gbk

print(s_gbk)
s_gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")   #将gbk编码转成utf-8
                                                      #先将gbk转化成Unicode再转换成utf-8
