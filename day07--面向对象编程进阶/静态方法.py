#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import os
# os.system()
# os.mkdir()

class Dog(object):
    def __init__(self,name):
        self.name = name

    @staticmethod #静态方法实际上把类的关系切断了，此函数只是单纯的函数了
                  #但仍需类名去调用该函数，调用时将实例对象传入，就又可以调用实例的属性
    def eat(self):
        print("%s is eating %s" %(self.name,'dd'))

    def talk(self):
        print("%s is talking"% self.name)
d = Dog("ChenRonghua")
d.eat(d)
d.talk()