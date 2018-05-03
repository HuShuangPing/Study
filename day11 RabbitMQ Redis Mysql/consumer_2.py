#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#模拟消费者断电
#实现消息公平分发
import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello',durable = True)


def callback(ch, method, properties, body):  #模拟断电，相当于没有完成回调函数
    print("-->",ch, method, properties)
    time.sleep(30)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  #手动确认

channel.basic_qos(prefetch_count=1)   #实现消息公平分发
channel.basic_consume(
                      callback,
                      queue='hello',
                      #no_ack=True    #不确认，一条消息处理完或没处理完都不会给服务器发消息
                       #一般不加，默认是自动确认
                     )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
#此时启动多个consumer，把第一个consumer挂起，服务器会自动把消息传送给第二个consumer
#只要客户端没有确认，服务端就不会把消息删除，
#问题：RabbitMQ怎么知道消费者断了？
#答：此时socket断了，socket连接着RabbitMQ，RabbitMQ就知道消费者断了
#