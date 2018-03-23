#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield     #[None]

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

c = consumer("Jack")
c.__next__()     #输出结果：Jack准备吃包子啦
c.__next__()     #输出结果：包子[None]来了,被[Jack]吃了!
                 #此时yield保存这个状态

# b1="韭菜馅"
# c.send(b1)     #从上个状态开始调用，并把b1值转入
#                #输出结果：包子[韭菜馅]来了,被[Jack]吃了!
# c.__next__()   #输出结果：包子[None]来了,被[Jack]吃了!

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("我开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了1个包子!，分两半")
        c.send(i)
        c2.send(i)

#实现单线程下实现并行
