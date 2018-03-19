#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import sys,time

for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)
'''
一般的文件流操作都包含缓冲机制，write方法并不直接将数据写入文件，而是先写入内存中特定的缓冲区。

flush方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区。

正常情况下缓冲区满时，操作系统会自动将缓冲数据写入到文件中。

至于close方法，原理是内部先调用flush方法来刷新缓冲区，再执行关闭操作，这样即使缓冲区数据未满也能保证数据的完整性。

如果进程意外退出或正常退出时而未执行文件的close方法，缓冲区中的内容将会丢失。
'''