#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)  #往fm104.5频道发消息
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()   #开始订阅，相当于打开收音机
        pub.subscribe(self.chan_sub)  #调频道
        pub.parse_response()         #准备接受，要在订阅者再写一次
        return pub