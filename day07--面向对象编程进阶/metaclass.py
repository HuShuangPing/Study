#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

class MyType(type):
    # 类的生成 调用 顺序依次是 __new__ --> __init__ --> __call__
    def __init__(self, what, bases=None, dict=None):
        print("--MyType init---")
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):   #__call__方法，对象加一个括号就可以调用
        print("--MyType call---")

        obj = self.__new__(self, *args, **kwargs)  #__new__是Python自带的一个方法，可以进行重构
        obj.data = {"name":111}
        self.__init__(obj, *args, **kwargs)


class Foo(object):
    __metaclass__ = MyType   #Foo类和MyType类通过__metaclass__相关联
                             #MyType相当于自己封装属于自己的类，以后的类用__metaclass__关联MyType类，相当于调用了这个自己定制的类
                             #例如，在MyType中obj.data = {"name":111}，所有关联__metaclass__的类都会有obj.data = {"name":111}

    def __init__(self, name):
        self.name = name
        print("Foo ---init__")

    def __new__(cls, *args, **kwargs):   #__new__方法实例化调用后，会优于__init__执行
                                         #通过__new__方法来调用__init__方法，将__new__方法屏蔽，对象将不能执行__init__方法
                                         #总：即通过__new__来创建对象的，大多数情况下不需要写__new__方法
        print("Foo --new--")
        #print(object.__new__(cls))
        return object.__new__(cls) #继承父亲的__new__方法
                                   #cls相当于把Foo传入，因为此时还没有实例化，故没有self



# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象
obj = Foo("Alex")
print(obj.name)