#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import gevent

def foo():
    print('Running in foo')
    gevent.sleep(2)  #模仿io
                     #遇到此操作，执行bar方法
    print('Explicit context switch to foo again')

def bar():
    print('Explicit精确的 context内容 to bar')
    gevent.sleep(1)   # 再次切换到foo方法
    print('Implicit context switch back to bar')

def func3():
    print("running func3 ")
    gevent.sleep(0)
    print("running func3  again ")


gevent.joinall([
    gevent.spawn(foo), #生成，发起
                       #先执行foo
    gevent.spawn(bar),
    gevent.spawn(func3),
])