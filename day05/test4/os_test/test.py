#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import os

print(os.getcwd())   #获取当前操作目录

#修改路径
os.chdir("G:\\考研")
#os,chdir(r"G:\考研")  #推荐使用
print(os.getcwd())
print(os.curdir)    #返回本目录:.
print(os.pardir)    #..

os.makedirs(r"G:\a\b\c\d")  #递归创建目录，在G盘文件不存在，但会递归创建

os.remove(r"G:\a\b\c\d")   #如果为空删除删除

os.mkdir(r"G:\考研\c")  #与makedirs不同的是，若文件目录不存在会报错