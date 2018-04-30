#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

from urllib import request

def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    f = open("url.html","wb")
    f.write(data)
    f.close()
    print('%d bytes received from %s.' % (len(data), url))

f('https://www.python.org/')