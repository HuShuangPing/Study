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

#