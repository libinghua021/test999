# -*- coding:utf-8 -*-

"""
实现登录接口对象封装
"""

import requests

# 登录接口对象
class ApiLogin(object):
    # 登录方法
    def api_post_login(self, url, mobile, code):
        # headers定义
        headers = {"Content-Type": "application/json"}
        # data定义
        data = {
                "mobile": mobile,
                "code": code
                }
        # 调用post并返回响应对象
        return requests.post(url, headers=headers, json=data)
