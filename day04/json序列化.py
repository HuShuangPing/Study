#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#序列化
#把信息写到硬盘上

#json  只能处理简单类型 字典 列表，字符串
#json适合所有语言，主要用来不同语言数据交互

#xml(一种存储数据的方式)真逐渐被json语言所替代

#如果想要处理复杂类型数据进行序列化，pickle
#pickle 和 json用法一样，可以将json换成pickle
import json
import pickle

def sayhi(name):
    print('hello',name)

info ={
    'name':"Jack",
    'age':22,
    'func':sayhi   #把内存地址当成value
                   #出现错误，原因是内存地址不是可序列化类型
}

with open("test.text","wb",encoding="utf-8") as f:
    f.write(json.dumps(info))   #无法存一个字典
    print(json.dumps(info))  #{"name": "Jack", "age": 22}