#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

# 可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象：

'''
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False
'''

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
'''
> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
'''

#Python的for循环本质上就是通过不断调用next()函数实现的，例如
'''

1
2
for x in [1, 2, 3, 4, 5]:
    pass
实际上完全等价于：

复制代码
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
复制代码

'''