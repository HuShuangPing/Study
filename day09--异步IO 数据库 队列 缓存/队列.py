#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#队列
# 解耦，使程序直接实现松耦合，
# 提高处理效率 ，
import queue

# q = queue.LifoQueue()   #后进先出
# #
# # q.put(1)
# # q.put(2)
# # q.put(3)
# # q.put(4)
# #
# # print(q.get())
# # print(q.get())
# # print(q.get())
# # print(q.get())  #输出结果为：4 3 2 1

q = queue.PriorityQueue()   #设置优先级

q.put((-1,"Jack"))
q.put((10,"Tom"))
q.put((12,"Mars"))
q.put((11,"Clark"))

print(q.get())
print(q.get())
print(q.get())
print(q.get())
       #输出结果
            # (-1, 'Jack')
            # (10, 'Tom')
            # (11, 'Clark')
            # (12, 'Mars')