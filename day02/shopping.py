#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HuShuangPing


salary = input("请输入工资:")
shopping_car=[]
product_list =[
    ("Iphone",5800),
    ("Mac Pro",9800),
    ("Bike",800),
    ("Watch",10600),
    ("coffe",31),
    ("book",120)
]

while True:
 for index,item in enumerate(product_list):
    print(index,item)
    user_choice=("请输入你的选择:")
    if user_choice.isdigit():
        user_choice= int(user_choice)
        if user_choice<len(product_list) and user_choice>-1:
            if product_list[user_choice][1]<salary :
              salary-=product_list[user_choice][1]
              shopping_car.append(product_list[user_choice])
              print("已添加%s商品到你的购物车，还有余额是：%s"%(product_list[user_choice],salary))
            else:
              print("你的余额还有%s,暂时不足够买其他商品，请及时充值",salary)
        else:
            print("你选择%s商品不存在",product_list[user_choice])
    elif user_choice == 'q':
           print("----------shoping list---------")
           for i in shopping_car:
              print(shopping_car)
              print("你的余额还有：%s",salary)
    else:
        print("请输入正确数字")