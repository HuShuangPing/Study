#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#形参 实参

def test(x,y):
    print(x)
    print(y)

#x,y是形参
 #1,2是实参
test(1,2)      #此处是形参与实参一一对应
test(y=2,x=1)  #关键参数调用，此处的y会赋给函数中的y,x也同样如此

#注：关键参数是不能调用的在形参前面
#test(x=2,3)  报错
test(4,y=4)   #没有报错