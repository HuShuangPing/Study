#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing

import re

# '.'-- 默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
#res = re.match("^.\d","JackAndRose")  #匹配一个字符
res = re.match(".+","Jac123Math123") #match()表示从头开始匹配，因此"^"这个符号在match中没有用
                                      #"+"表示一个或多个，这个表达式是匹配任意字符，后面\d没有用到
print(res)

# '$' --匹配字符结尾(是指整个字符串的结尾)
res2 = re.search("M[a-zA-Z]+h","Jac123Math123")   #search()从整个文本中开始搜索,但只搜索一次就返回
# 只会匹配到第一个Math
print(res2)

#'?' --匹配前一个字符1次或0次
res3 = re.search("jjj?","jjackjjjjjack")  #匹配到第一个j
#匹配的是"?"前的j的前"jj"的字符，匹配到的结果jj
print(res3)

#'{m}'--匹配前一个字符m次
res4 = re.search("[0-9]{3}","jack1jakc123jack2")
print(res4)  #匹配到3个连续是数字

res5 = re.findall("[0-9]{1,3}","jack123jack1jack1234")  #匹配1到3个数字
print(res5)  #findall是搜索到全部符合要求的
#匹配到'123', '1', '123', '4'

#'|' --匹配|左或|右的字符，符合其中一个条件就可以
res6 = re.search("abc|ABC","ABCBabcCD").group()
print(res6) #输出结果是ABC

res6 = re.findall("abc|ABC","ABCBabcCD")  #用findall方法就不能用group方法
print(res6)  #匹配到'ABC', 'abc'

#'(...)' --分组匹配
res7 = re.search("abc{2}","Jackabcc")  #匹配到abcc
print(res7)
res7 = re.search("(abc){2}","Jackabcabc") #匹配到abcabc
print(res7)
res7 = re.search("(abc){2}\|","jackabcabc|")  #匹配到abcabc|
print(res7)
#有多个转义字符需要逐一使用\
res7 = re.search("(abc){2}(\|\|\=){2}","jackabcabc||=||=")
print(res7)  #匹配到abcabc||=||=

# '\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
# '\Z'    匹配字符结尾，同$

# '\d'    匹配数字0-9
# '\D'    匹配非数字

#'\w'    匹配[A-Za-z0-9]

#'s'     匹配空白字符、\t、\n、\r ,
res8= re.search("\s+","ab\tc1\n3")
print(res8)   #匹配到\t

#'(?P<name>...)' 分组匹配
res9 = re.search("(?P<id>[0-9]+)","abc1234abc@1")
print(res9)  #匹配到1234

res9 = re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)","abcd1234daf034").groupdict()
print(res9)   #输出结果：{'id': '1234', 'name': 'daf'}

res9 = re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city")
print(res9)  #{'province': '3714', 'city': '81', 'birthday': '1993'}n



##re.split()  以匹配到的字符当做列表分隔符
res10 = re.split("[0-9]+","abc123fsh12sh")
print(res10)   #['abc', 'fsh', 'sh']

#re.sub      匹配字符并替换
res11 = re.sub("[0-9]+","|","abc1232ff43sd")
print(res11)   #输出结果abc|ff|sd
res11 = re.sub("[0-9]+","|","abc1232ff43sd",count=1)
print(res11)   #输出结果abc|ff43sd

#几个匹配模式
  #re.IGNORECASE: 忽略大小写（括号内是完整写法，下同）
res12 = re.search("[a-z]+","abcA",flags=re.IGNORECASE)
print(res12)  #匹配到abcA
# re.MULTILINE: 多行模式
res12 = re.search(r"a","\nabc\neee",flags=re.MULTILINE)
print(res12) #匹配到a，不然会匹配不到
#S(DOTALL): 点任意匹配模式，改变'.'的行为
   #'.'匹配到任意字符，除换行符之外
res12 = re.search(r".+","\nabc\neee",flags=re.DOTALL)
print(res12)   #匹配到\nabc\neee

