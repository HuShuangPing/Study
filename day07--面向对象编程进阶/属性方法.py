#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import os
# os.system()
# os.mkdir()

class Dog(object):
    '''这个类是描述狗这个对象的'''

    def __init__(self,name):
        self.name = name
        self.__food = None

    #@staticmethod #实际上跟类没什么关系了
    #@classmethod
    @property #attribute，属性方法把一个方法变成一个静态属性，不能通过对象来调用
              #调用：d.eat
              #若属性方法中有参数，对象不能传入参数
    def eat(self):
        print("%s is eating %s" %(self.name,self.__food))
    @eat.setter   #属性方法中的参数单独写一个方法
                  #调用：d.eat
                  #      d.eat="baozi"
    def eat(self,food):
        print("set to food:",food)
        self.__food = food
    @eat.deleter  #删除属性方法的属性
    def eat(self):
        del self.__food
        print("删完了")

    def talk(self):
        print("%s is talking"% self.name)

    def __call__(self, *args, **kwargs):
        print("running call",args,kwargs)

    def __str__(self):
        return "<obj:%s>" %self.name

#print(Dog.__dict__) #通过类调用，打印类里的所有属性，不包括实例属性
d = Dog("ChenRonghua")
print(d)
print(Dog.__doc__)   #打印类的描述信息
# print(d.__dict__) #通过实例调用，以字典形式打印所有实例属性，不包括类属性
# d(1,2,3,name=333)   #调用__call__的成员方法

#Dog("ChenRonghua")()
