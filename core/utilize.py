# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 17-12-3 下午9:41
# Author: sty
# File: utilize.py
# 模拟用户的帐号信息

import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 获得当前目录的父目录
# 初始化json文件
def utilize():
    user_data = [
        {'user_account': '10001','user_name': 'jack', 'user_login_pwd': '123',
         'user_pay_password': '123456','user_credit': 15000, 'is_freeze': 0, 'balance': 0,'time': '2017-01-01 0:0:0'},
        {'user_account': '10002', 'user_name': 'tom', 'user_login_pwd': '321',
         'user_pay_password': '654321', 'user_credit': 15000, 'is_freeze': 0, 'balance': 0, 'time': '2017-01-01 0:0:0'}
    ]

    data_location = BASE_DIR + '//data//user_info.json'  #将user的信息保存的文件位置
    with open(data_location, 'w') as f:
        json.dump(user_data, f)

#utilize()