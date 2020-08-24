# -*- coding:utf-8 -*-

"""
目标：完成登录业务层实现
"""

import unittest
from api.login import ApiLogin

# 登录测试类
class TestLogin(unittest.TestCase):
    # 新建测试方法
    def test_login(self):
         #暂时存放数据url、mobile、code
        url="http://ttapi.research.itcast.cn/app/v1_0/authorizations"
        mobile = '13338053699'
        code = "189598"    //这里需要先在浏览器输入http://ttapi.research.itcast.cn/app/v1_0/sms/codes/13480。。。来获取验证码，然后才开始执行
         #调用登录方法
        s = ApiLogin().api_post_login(url, mobile, code)
        print("响应结果：", s.json())
         #断言 响应信息  状态码
        self.assertEqual("OK",s.json()['message']);
        self.assertEqual(201,s.status_code);
if __name__ == '__main__':
    unittest.main();