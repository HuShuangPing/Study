#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#用协程并发爬取网页

from urllib import request
import gevent,time
from gevent import monkey

monkey.patch_all() #把当前程序的所有的io操作给我单独的做上标记

def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://github.com/' ]
time_start = time.time()
for url in urls:   #串行执行
    f(url)
print("同步cost",time.time() - time_start)


#异步执行爬虫
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),
])
print("异步cost",time.time() - async_time_start)