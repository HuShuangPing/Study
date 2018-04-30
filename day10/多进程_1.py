#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import multiprocessing
import time

def run(name):
    time.sleep(2)
    print("hello",name)

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run,args=("Jack %s"%i,))   #启动多线程
        p.start()
    #    p.join()
