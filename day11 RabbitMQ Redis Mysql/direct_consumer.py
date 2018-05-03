#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]   #获取执行这个脚本的参数
if not severities:    #没有参数
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])  #报错
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs',  #每个参数绑定到exchange，可以接受服务端不同的消息
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()