#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import copy

person =["name",['saving',100]]
'''
#三种复制（浅拷贝）
p1 = copy.copy(person)
p2=person[:]
p3=list(person)
'''
p1=person[:]
p2=person[:]

p1[0] ="Alex"
p2[0] = "fengjie"

print(p1)    #输出的结果是p1.p2都各自对第一个元素进行改变
print(p2)

p1[1][1] = "50"

print(p1)    #输出的结果内嵌的列表中第二元素p1,p2都发生了改变
print(p2)