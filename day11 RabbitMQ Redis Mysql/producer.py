#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))  #相当于建立一个socket
channel = connection.channel()  #声明一个管道

# 声明queue
channel.queue_declare(queue='hello')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',   #queue名
                      body='Hello World!')   #消息内容
print(" [x] Sent 'Hello World!'")
connection.close()   #关闭管道