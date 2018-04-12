#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..."%self.name,food)


d = Dog("NiuHanYang")
choice = input(">>:").strip()

if hasattr(d,choice):      #判断object中有没有一个name字符串对应的方法或属性
    getattr(d,choice)      #根据字符串去获取obj对象里的对应的方法的内存地址
    getattr(d, choice)()   #执行对应的方法

else:
    setattr(d,choice,bulk) #d.choice = bulk,创建一个类中没有的方法
    d.talk()   #输入时talk,则调用的talk方法
    func = getattr(d, choice)
    func(d)   #可以传入参数执行对应的方法

    setattr(d,choice,22)
    print(getattr(d,choice))   #打印值为22，是静态属性，就直接把值返回