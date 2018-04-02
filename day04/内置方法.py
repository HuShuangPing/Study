#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


#all()        #可迭代对象中所有元素都为真返回真
print(all([0,-5,3]))   #输出结果：False 非0为真，0为假

#any()         #列表或可迭代对象任一数据为真返回真
print(any([0,-5,3]))  #输出结果为：True

#ascii()
print(ascii([1,2,"中国"]))  #把内存对象变成一个可打印的对象
                            #输出结果：[1, 2, '\u4e2d\u56fd']

#bin()     #十进制转换成二进制
print(bin(255))  #输出结果：0b11111111

#bool()   #判断真假，0假，非0真，还可以判断列表是否为空
print(bool([ ]))   #输出结果为：False

#bytearry  #字节数组
a = bytes("abcd",encoding="utf-8")
print(a.capitalize(),a)  #a.capitalize是对a字符字符串进行大写，再次打印a，a没有改变，bytes字符串不可修改

b = bytearray("abcd",encoding="utf-8")
print(b[0])   #输出为：97,字母a的ASCII码
b[1] = 100  #此时'b'改为'd'

#callable()    判断是不是可以调用
def sayHello():pass
print(callable(sayHello))   #输出结果：True

#chr()   输出数字对应的ASCII码
print(chr(97))   #输出结果：a

#ord()     输出字符对应ASCII码的数字
print(ord('a'))  #输出结果为:97

#classmethod()   类方法在以后会讲到

#compile()   函数将一个字符串编译为字节代码。

#complex()   复数

#delattr()


#dict()   生成一个默认字典

#dir()
a=()
print(dir(a))   #查看子弹中有哪些默认的方法

#divmod(a,b)
print(divmod(5,2))   #输出结果为（2,1）
                     #第一个数字是商，第二个是余数
print(divmod(4,2))   #输出结果为（2,0）

#enumerate() 将可循环序列sequence以start开始分别列出序列数据和数据下标

#eval()   把一个字符串转化成字典

#filter()  过滤
#前提：匿名函数（用完就删除）
res = filter(lambda n:n>5,range(10)) #lambda表示匿名函数，冒号前面的x表示函数参数。
for i in res:
    print(i)

# 匿名函数
calc = lambda n:print(n)
calc(5)

#map()
#将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
fes = map(lambda n:n*n,range(10))
for i in fes:
    print(i)
#reduce()
#reduce函数会对参数序列中元素进行累积
import functools
ges = functools.reduce(lambda x,y:x+y,range(10))
print(ges)

#frozenset
a = frozenset([1,2,4,5,5])

#globals() 返回当前程序的所有的变量的key,value
print(globals())

#hash() 散列
print(hash("ert"))

#hex()  把一个数转换成十六进制
print(hex(255))

#locals()
def test():
    local_var =55
    print(locals())   #打印局部变量
test()
print(globals().get("local_var"))  #globals() 打印全局变量
print()

#round()  保留整数位
print(round(1.3434233))
print(round(1000.2))

#sorted()



#zip()
a=[1,2,3,4]
b=['c','d','c','r']
for i in zip(a,b):
     print(i)
#输出结果
#(1, 'c')
#(2, 'd')
#(3, 'c')
#(4, 'r')