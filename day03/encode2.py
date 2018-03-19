#!/usr/bin/env python
# -*- coding:gbk -*-
# Author:HuShuangPing

import sys
print(sys.getdefaultencoding())
_author_="Alex"

s = "你好"   #虽然文件的编码是gbk，但Python内置的还是Unicode编码
             #此时s还是Unicode编码
print(s.encode("gbk"))  #此时将字符串编码Unicode转换成gbk编码
                        #打印出是bytes类型是gbk的表现形式
print(s.encode("utf-8")) #和上面gbk原理相同
print(s.encode("utf-8").decode("utf-8").encode("gb2312"))