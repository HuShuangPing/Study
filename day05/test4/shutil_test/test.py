#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing
import shutil


# shutil
# 高级的 文件、文件夹、压缩包 处理模块


# shutil.copyfileobj(fsrc, fdst[, length])
# 将文件内容拷贝到另一个文件中，可以部分内容
with open("模块","r",encoding="utf-8") as f1:
     with open("模块_copy","w",encoding="utf-8") as f2:
        shutil.copyfileobj(f1,f2)


# shutil.copyfile(src, dst)
# 拷贝文件

#shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的