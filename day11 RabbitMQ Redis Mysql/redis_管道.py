#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

r = redis.Redis(connection_pool=pool)


pipe = r.pipeline()

pipe.set('name', 'alex')
time.sleep(10)
pipe.set('role', 'sb')

pipe.execute()