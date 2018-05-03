#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


#消息持久化
#在客户端和服务端声明队列时都进行 durable = True
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))  #相当于建立一个socket
channel = connection.channel()  #声明一个管道

# 声明queue
channel.queue_declare(queue='hello',durable = True)   #durable = True 这个作用是将队列持久化，没有把消息持久化

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',   #queue名
                      body='Hello World!',
                      properties = pika.BasicProperties(
                          delivery_mode=2,  # 使消息持久化
                        ))   #消息内容
print(" [x] Sent 'Hello World!'")
connection.close()   #关闭管道