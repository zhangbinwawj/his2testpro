import sys
import unittest
from time import sleep

from test_case.models import myunit, function
from test_case.page_obj.loginPage import login

sys.path.append("./models")
sys.path.append("./page_obj")
# import sys
# from os import path
# sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
"""业务层：用于存放我们真正的测试用例的操作部分"""


class loginTest(myunit.MyTest):
    """登录测试"""

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        """用户名密码为空登录"""
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.user_error_hint(), "请输入用户名！")
        self.assertEqual(po.pawd_error_hint(), "请输入用户名！")
        function.insert_img(self.driver, "账号密码为空.png")

    def test_login2(self):
        """用户与密码不匹配"""
        # character = random.choice('')
        username = '1002'
        self.user_login_verify(username=username, password='1234564')
        po = login(self.driver)
        self.assertEqual(po.pawd_error_hint(), "用户或密码错误!")
        function.insert_img(self.driver, "密码已账号不匹配.png")

    def test_login3(self):
        """用户密码正确登录成功"""
        self.user_login_verify(username="1002", password="654321")
        sleep(3)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), "杨华君")
        function.insert_img(self.driver, "登录成功.png")


if __name__ == "__main__":
    unittest.main()
