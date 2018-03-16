#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

list_1 = [1,3,4,2,3,4,2,55,3,6]

list_1 = set(list_1)           #将列表设置为集合，去掉重复集合
print(list_1,type(list_1))     #typeday序列的类型。集合和字典一样是无序的

list_2 = set([3,2,4,4,55,10,9])
#取两个集合的交集
print(list_1.intersection(list_2))

#将两个集合合并，并去重
print(list_1.union(list_2))

#差集，在list_1中存在，在list_2中不存在的
print(list_1.difference(list_2))

#子集，判断list_1是不是list_2的子集
print(list_1.issuperset(list_2))

#对称差集,将两个集合都有的元素去掉，剩下的就是对称差集
print(list_1.symmetric_difference(list_2))

list_3 = set([1,2,3,4])
list_4 = set([5,6,7])
print(list_3.isdisjoint(list_4))   #两个集合没有交集返回True，有交集返False

#用运算符求交集，并集,差集，对称差集
#交集
print(list_1 & list_2)
#并集
print(list_1 | list_2)
#差集
print(list_1 - list_2)
#对称差集
print(list_1 ^ list_2)

#集合没有插入，只有添加
list_1.add(555)
list_1.update(4444)

#删除
list_1.remove(555)       #元素不存在会报错
list_1.pop()   #随机删除
list_1.discard(4444)    #元素不存在不会报错，None



