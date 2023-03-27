import sys
import unittest
from time import sleep

from test_case.models import myunit, function
from test_case.page_obj.loginPage import login
from test_case.page_obj.registrationPage import RegisterAction


class RegisterActionTest(myunit.MyTest):
    """注册挂号模板测试"""

    # 切换到注册挂号菜单
    def toggle_menu(self):
        RegisterAction(self.driver).registration_menu()
        RegisterAction(self.driver).register_menu()

    # 点击注册按钮
    def toggle_button(self):
        RegisterAction(self.driver).register_button()

    # 注册必填项为空
    def test_register1(self):
        """注册信息为空，注册"""
        # 登录系统
        userlogin = login(self.driver)
        userlogin.user_login(username='1002', password='654321')

        # 切换菜单
        self.toggle_menu()
        ol = RegisterAction(self.driver)
        self.driver.switch_to.frame(ol.ifranme())  # 切换到ifrname表单

        self.toggle_button()
        self.assertEqual(ol.required_error_hint(), "该输入项为必输项")
        function.insert_img(self.driver, "必填项为空.png")
        # self.driver.switch_to.parent_frame()


if __name__ == "__main__":
    unittest.main()



