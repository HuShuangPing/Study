#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

#字典
info={
    'stu101':"周杰伦",
    "stu102":"陈奕迅",
    "stu103":"王菲"
}
print(info)   #打印的结果是无序的，即字典无下标
print(info["stu102"])

#修改
info["stu102"]="林俊杰"

#添加
info["stu104"] ="四块钱"  #不存在即添加

#删除
#del info  #删除字典
#info.pop("stu101")  #第二种删除指定元素
#info.popitem()      #随机删除

#查找
print(info["stu102"])      #若元素不存在会报错
print(info.get("stu101"))  #元素存在返回元素值，若不存在返回空值
print("stu110" in  info)   #判断元素在不在序列中