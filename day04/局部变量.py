#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


def change(name):
    print("before name:",name)
    name = "Jack Hu"                  #此处的name就是局部变量，只在函数内生效
    print("after name：",name)
    global school         #在函数内声明一个全局变量
                          #不要在函数内对全局变量进行修改
                          #在函数外对全局变量进行修改


name="Jack"
change(name)       #第二个打印值为Jack Hu
print(name)

school = "QingHua"
print("school:",school)