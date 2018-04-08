#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

# class People: 经典类
class People(object): #新式类
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []
        print("--doens't run ")
    def eat(self):
        print("%s is eating..." % self.name)
    def talk(self):
        print("%s is talking..." % self.name)
    def sleep(self):
        print("%s is sleeping..." % self.name)

class Relation(object):
    def __init__(self,n1,n2):
        print("init in relation")
    def make_friends(self,obj): #w1 没有进行初始化，但在子类中已进行了初始化，父类没有构造方法就会执行子类的，有就执行自己的构造方法
        print("%s is making friends with %s" % (self.name,obj.name))
        self.friends.append(obj.name)

class Man(Relation,People):   #继承在括号内写父类名，可以多继承，执行的顺序是从左到右
                              #父类Ration若有构造方法，即时People中有构造方法，子类只会继承Relation的构造方法
    # def __init__(self,name,age,money):      #重构，Man类中有的属性，但Women类中没有的属性，需对原初定义重构，要将原来有的属性都写上
    #     #（第一种重构写法：)People.__init__(self,name,age)
    #       (第二种重构方法：)super(Man,self).__init__(name,age) #新式类写法（推荐，要是多继承，无需多次写父类名）
    #     self.money  = money
    #     print("%s 一出生就有%s money" %(self.name,self.money))
    def piao(self):
        print("%s is piaoing ..... 20s....done." % self.name)
    def sleep(self):
        People.sleep(self)       #调用父类方法，父类和子类方法都会执行一次
        print("man is sleeping ")
class Woman(People,Relation):
    def get_birth(self):
        print("%s is born a baby...." % self.name)

m1 = Man("NiuHanYang",22)
# w1 = Woman("ChenRonghua",26)   #Man类使用父类方法
#
# m1.make_friends(w1)
# w1.name = "陈三炮"
# print(m1.friends[0])
