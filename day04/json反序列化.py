#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#反序列化
#把内容从硬盘上加载回来

import json
with open("test.text","r",encoding="utf-8") as f:
    data = json.loads(f.read())
    print(data['age'])

