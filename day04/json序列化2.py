#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

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
    pickle.dump(info,f)  #第一个参数是序列化对象
                         #第二个参数是文件
    #等价于f.write(pickle.dumps(info))