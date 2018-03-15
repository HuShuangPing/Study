#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#列表[]

names =["张三","王五","李四","赵谦","周五","周五"]

print(names[0],names[2])
print(names[-1])  #最后一个元素
#切片
print(names[:])  #全取
print(names[:3])    #从0开始取
print(names[-2:])   #取最后连个元素

#添加
names.append("张二麻子")  #直接在最后一个元素添加
print(names)

names.insert(1,"老王")   #第一个参数是选择插入的位置
print(names)

#改
names[2] ="老李"
print(names)

#删除
names.remove("张二麻子")  #直接删除元素
del names[1]
names.pop(2)            #不输入删除位置，默认是最后一个元素


#查
print(names.index("赵谦"))   #根据元素查位置
print(names.count("周五"))  #返回与"周五"同名的个数

#其他
names.clear()  #清空

names.reverse()   #翻转

names.sort()    #排序 ACII码大小进行排序

names2 = [1,2,3,4,5]

names.extend(names2)   #将names2和names表进行合并，但name2表还在