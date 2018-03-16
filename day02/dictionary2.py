#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#字典
'''
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
#嵌套修改
av_catalog["大陆"]["1024"][1]= "可以在国内做镜像"
print(av_catalog)

av_catalog.setdefault("台湾:",{"wwww.223.com":[1,2]})
print(av_catalog)
'''
info={
    'stu101':"周杰伦",
    "stu102":"陈奕迅",
    "stu103":"王菲"
}
b = {
    "stu101":"阿信",
    1:3,
    2:5
}
info.update(b)    #将b当做参数传入到a中，即有相同元素进行更新，没有进行创建
print(info)

c = dict.fromkeys([6,7,8],[1,{"name":"alex"},444])   #fromkeys初始化一个字典,本式中是列表中嵌套一个字典
print(c)
c[7][1]["name"] = "Jack Chen"
print(c)     #打印结果是都修改为Jack Chen ,三分共享一个内存

for i in info:
    print(i)   #打印出key值
    print(i,info[i])  #打印出key和value值
for k,v in info.items():
    print(k,v)   #效率低，遍历字典

print(info.items())   #把一个字典转化为一个列表