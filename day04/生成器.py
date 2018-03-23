#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#生成器generator
#    只有在调用时才会生成响应的数据
#    生成器只保存当前的数据，不能往前查看数据
#                            但可以往后加载数据，即，c.__next__()
#功能：通过生成器实现并行的效果

#推算的算法复杂，可以用函数来写生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b       #报存了函数的中断的状态
        a, b = b, a + b    #t = (b, a + b)  t是一个tuple
                           # a = t[0]
                           # b = t[1]
        n = n + 1
    #return 'done'         #此处的return是报错的时候返回done

#fib(10)  #10是生成10斐波那契数，从0开始
# 著名的斐波拉契数列（Fibonacci）
#     除第一个和第二个数外，任意一个数都可由前两个数相加得到：
#     1, 1, 2, 3, 5, 8, 13, 21, 34, ..

f = fib(10)
# print(f.__next__())   #每调用一次next生成一个斐波那契数
# print(f.__next__())
# print(f.__next__())
#
# for i in f:
#     print(i)

#异常处理：要是打印的次数超过定义值，进行异常处理
g=fib(6)
while True:
   try:
       x = next(g)
       print('g:', x)
   except StopIteration as e:
       print('Generator return value:', e.value)
       break