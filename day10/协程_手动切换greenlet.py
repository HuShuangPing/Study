#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing
from greenlet import greenlet
def test1():
    print(12)
    gr2.switch() #切换到test2，执行test2操作
    print(34)
    gr2.switch() #切换到test2停的位置，即gr1.switch()
def test2():
    print(56)
    gr1.switch() #切换到test1停的位置，即gr2.switch()
    print(78)

gr1 = greenlet(test1) #启动一个协程
gr2 = greenlet(test2)
gr1.switch()         #手动切换到test1
#s输出结果为：
            # 12
            # 56
            # 34
            # 78