#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import os
# os.system()
# os.mkdir()

class Dog(object):
    #n = 333
    #name = "huazai"
    def __init__(self,name):
        self.name = name
        #self.n  = 333#@staticmethod #实际上跟类没什么关系了

    @classmethod   #类方法：只能访问类变量，不能访问实例变量
    def eat(self):
        print("%s is eating %s" %(self.name,'dd'))

    def talk(self):
        print("%s is talking"% self.name)


d = Dog("ChenRonghua")
d.eat()