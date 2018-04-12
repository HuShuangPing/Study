#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import module_test
#当有多处引入模块
from module_test import test

def logger():
    test()
    print("in the logger")

def search():
    test()
    print("in the search")