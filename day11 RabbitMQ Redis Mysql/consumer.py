#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ？‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello')  #要是生产者没有声明这个queue，消费者就自己声明一个queue
                                      #要是生产者声明了这个queue，消费者这个queue就什么都不干


def callback(ch, method, properties, body):
    print("-->",ch, method, properties)
    print(" [x] Received %r" % body)


channel.basic_consume(  #消费消息
                      callback,   #如果收到消息，就调用ccallback函数来处理消息
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()   #开始收消息，会一直收，没有消息就卡在那