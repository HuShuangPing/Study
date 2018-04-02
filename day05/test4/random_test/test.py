#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import random

print(random.random())   #随机浮点0,1

print(random.randint(1,3))  #包括1,3

#range(1,3)  #顾头不顾尾，不包括3

print(random.choice("hello"))   #choice()可传入序列

random.sample("hello",2)  #从传入的系列中随机取两个

a=[1,2,3,4,5]
a = random.shuffle(a)  #洗牌功能