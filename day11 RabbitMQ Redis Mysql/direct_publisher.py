#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')  #类型

severity = sys.argv[1] if len(sys.argv) > 1 else 'info' #要是参数长度大于1，默认取执行这个脚本的参数，
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,   #把消息都发送到severity
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()