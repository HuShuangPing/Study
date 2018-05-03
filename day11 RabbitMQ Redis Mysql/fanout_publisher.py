#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',   #
                         type='fanout')   #类型

message = ' '.join(sys.argv[1:]) or "info: Hello World!"   #
channel.basic_publish(exchange='logs',
                      routing_key='',  #没有queue，也没有声明queue
                      body=message)
print(" [x] Sent %r" % message)
connection.close()