#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')   #类型

result = channel.queue_declare(exclusive=True)
# exclusive 唯一的，排他的
# 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除

queue_name = result.method.queue

channel.queue_bind(exchange='logs',   #绑定到转发器上，即exchange
                   queue=queue_name)  #

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()