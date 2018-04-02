#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#将数据多次加载出来

#注：数据可以多次dump，但只能load一次
#写程序dump一次，load一次
#可以用文件将之前数据冲掉

import json

with open("test.text","r",encoding="utf-8") as f:
    data = json.load(f)  #等价于pickle.loads(f.read())
    print(data['age'])   #报错