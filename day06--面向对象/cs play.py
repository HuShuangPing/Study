#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

class Role:
    n = 123 #类变量,不用实例化就可以使用
    n_list = []
    name = "我是类name"
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        #构造函数
        #self是为了接受对象本身
        #在实例化时做一些类的初始化的工作
        self.name = name #r1.name=name实例变量(静态属性),作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value   #设置私有属性,在属性名前加" __"
                                         #外部对象不能调用，在类的内部可以调用
        self.money = money
    def __del__(self):    #析构函数
                          #析构函数无论调用不调用，都会执行，而且在对象释放或销毁的时候执行
          #self是接受对象
        pass #print("%s 彻底死了。。。。" %self.name)

    def show_status(self):  #类方法(动态属性)
        print("name:%s weapon:%s life_val:%s" %(self.name,
                                                 self.weapon,
                                                self.__life_value))    #通过定义一个方法，让外部对象来查看私有属性的值
    def __shot(self):    #私有方法，在方法名前"__"
        print("shooting...")

    def got_shot(self):
        self.__life_value -=50
        print("%s:ah...,I got shot..."% self.name)

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name,gun_name) )

print(Role.n)    #打印的结果是123


r1 = Role('Chenronghua', 'police',  'AK47') # Role(r1,'Alex', 'police',  'AK47')把一个类变成一个具体对象的过程叫 实例化(初始化一个类，造了一个对象)
r1.buy_gun("AK47")
r1.got_shot()
r1.__shot()    #实际是Role.__shot(r1)
print(r1.show_status())



r2 = Role('jack', 'terrorist', 'B22')  #生成一个角色 ，实际是Role(r2,"jack","terrorist","B22")
r2.got_shot()
# r1.name = "陈荣华"
# r1.n_list.append("from r1")
# r1.bullet_prove = True    #实例自己加一个属性
# r1.n = "改类变量"       #相当于在r1在自己内存中创建一个新的变量
# print("r1:",r1.weapon,r1.n )
# #del r1.weapon             #实例自己删除一个属性
#
#
#
#
# #print(r1.n,r1.name,r1.bullet_prove,r1.weapon)
#
# #
# r2 = Role('jack', 'terrorist', 'B22')  #生成一个角色
# r2.name = "徐良伟"
# r2.n_list.append("from r2")         #打印结果为包括r1追加的值
                                      #r1,r2共享一个内存
# print("r2:",r2.name,r2.n,r2.n_list)   #r1中类变量改变
                                        #r2中类变量没有改变
# # r2.got_shot() #Role.got_shot(r2)
#
# Role.n = "ABC"
# print(Role.n_list)
#
# print(r1.n ,r2.n )
