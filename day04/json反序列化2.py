#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import pickle
with open("test.text","r",encoding="utf-8") as f:
    data = pickle.load(f)  #等价于pickle.loads(f.read())
    print(data['age'])
