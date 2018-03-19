#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

f = open("yesterday2","r",encoding="utf-8")
#打开一个空白的新文件
f_new = open("yesterday.bak","w",encoding="utf-8")

for line in f:
    if "当我年轻时" in line:
        line = line.replace("当我年轻时","当Alex年轻时")
    f_new.write(line)
f.close()
f_new.close()