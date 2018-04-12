#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

class JackError(Exception):    #若和系统异常相同，不会对系统异常覆盖
    def __init__(self, msg):
        self.message = msg
    # def __str__(self):   __str__调用后直接打印值
    #     return 'sdfsf'
try:
    raise JackError('数据库连不上')
except JackError as e:
    print(e)   #sdfsf