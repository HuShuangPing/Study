#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#自动关闭文件
with open("yesterday2","r",encoding="utf-8") as  f,\
      open("yesterday","r",encoding="utf-8") as f2:       #打开多个文件
    for line in f:
        print(line)