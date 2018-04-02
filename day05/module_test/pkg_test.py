#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


import package_test
#实际上是run __init__.py

#package_test.test1.test()  #报错
#导包和导模块
#导模块就是把模块内代码导入
#导包就是运行 __init__.py文件

#在package包内的__init__.py内将test1文件导入
#from . import test1
package_test.test1.test()