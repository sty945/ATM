# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 17-12-2 上午9:50
# Author: sty
# File: shopping_car.py

# 1.用户入口
#   商品信息存在文件里
#   已购商品，余额记录
# 2.商家入口
#   可以添加商品,修改商品价格

import json


def init_shop_list():
    items = [
        {'num': 1, 'name': '衣服', 'price': 239},
        {'num': 2, 'name': '鞋子', 'price': 139},
        {'num': 3, 'name': '帽子', 'price': 39},
        {'num': 4, 'name': '书包', 'price': 99},
        {'num': 5, 'name': '袜子', 'price': 9},
        {'num': 6, 'name': '电脑', 'price': 5239},
        {'num': 7, 'name': '水杯', 'price': 9},
    ]
    with open('item_data.json', 'w') as f:
        json.dump(items, f)
def init_costumer_shop_list(balance=5000):
    items = {'balance': balance, 'items':[{'name': 'none', 'price': 0, 'cnt': 0}], 'total_items': 0}
    with open('shop_list.json', 'w') as f:
        json.dump(items, f)

def write_file(data, file = 'item_data.json'):
    with open(file, 'w') as f:
        json.dump(data, f)

def read_file(file = 'item_data.json'):
    with open(file, 'r') as f:
        items = json.load(f)
        if file == 'item_data.json':
            items.sort(key=lambda x: x['num'])
    return items

def is_exit(exit):
    if exit == 'y':
        return 1
    else:
        return 0

def costomer():
    items = read_file()
    balance = int(input('salary:'))
    info = read_file('shop_list.json')
    info['balance'] = balance
    write_file(info, 'shop_list.json')
    while True:
        info = read_file('shop_list.json')
        print(info)
        for item in items:
            print(item['num'], item['name'], item['price'])
        while True:
            item_select = int(input('select item num you choose:'))
            if item_select not in range(0, items[-1]['num'] + 1):
                print('您输错了，请重新输入')
            else:
                break
        for item in items:
            if item['num'] == item_select:
                if item['price'] > info['balance']:
                    print('your money is not enough')
                else:
                    info['balance'] = info['balance'] - item['price']
                    if info['total_items'] == 0:
                        info['items'].clear()
                    new_item = {'name': item['name'], 'price': item['price']}
                    info['items'].append(new_item)
                    info['total_items'] += 1
        write_file(info, 'shop_list.json')
        info = read_file('shop_list.json')
        print('your balance is ', info['balance'])
        print('you have buyed %s items:' % info['total_items'])
        for item in info['items']:
            print('name: {name}, price: {price}'.format(name=item['name'], price=item['price']))
        while True:
            exit = input("exit or not(y , n):")
            if exit != 'y' and exit != 'n':
                print('您输错了，请重新输入')
            else:
                break
        if is_exit(exit):
            break

def shop():
    items = read_file()
    while True:
        chice = input('---输入：1 修改， 2 添加，3 删除， 4 查找, q 退出---:')
        print('当前商品为：')
        for item in items:
            print(item)
        if chice == '1':
            num = input('请输入要修改商品的序号')
            for item in items:
                if item['num'] == int(num):
                    print('当前商品为：', item['name'])
                    price = int(input('请输入修改后的价格:'))
                    item['price'] = int(price)
            write_file(items)
        elif chice == '2':
            num = int(input('请输入新商品的序号：'))
            name = input('请输入新商品的名字：')
            price = int(input('请输入新商品的价格:'))
            new_item = {'num': num, 'name': name, 'price': price}
            items.append(new_item)
            write_file(items)
        elif chice == '3':
            num = input('请输入要删除商品的序号')
            for item in items:
                if item['num'] == int(num):
                    print('当前商品为：', item['name'])
                    del item
                    print('删除成功')
            write_file(items)
        elif chice == '4':
            num = input('请输入要查找商品的序号')
            for item in items:
                if item['num'] == int(num):
                    print('当前商品为：{name}, 价格为：{price}'.format(name=item['name'], price=item['price']))
        elif chice == 'q':
            break


if __name__ == '__main__':
    while True:
        init_shop_list()
        init_costumer_shop_list()
        chice = input('input 1:customer, 2:shop, q:exit:')
        if chice == '1':
            costomer()
        elif chice == '2':
            shop()
        elif chice == 'q':
            break