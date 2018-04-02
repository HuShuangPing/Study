#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#将数据多次存入

import json

def sayhi(name):
    print('hello',name)

info ={
    'name':"Jack",
    'age':22,
   # 'func':sayhi   #把内存地址当成value
                   #出现错误，原因是内存地址不是可序列化类型
}

with open("test.text","w",encoding="utf-8") as f:
    json.dump(info,f)      #等价于f.write(pickle.dumps(info))
    json.dump(info,f)

