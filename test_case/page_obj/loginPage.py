from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from test_case.page_obj.base import Page


class login(Page):
    """
    Page层：用于存放页面元素定位，测试系统页面封装操作到的元素
    """

    url = 'http://192.168.137.130:8080/his2/login.jsp'

    # bbs_login_user_loc = (By.XPATH, "html/body/form/div[2]/table[1]/tbody/tr[1]/td[2]/input")
    # bbs_login_button_loc = (By.ID, 'j_login')
    #
    # def bbs_login(self):
    #     self.find_element(*self.bbs_login_user_loc).click()
    #     sleep(3)
    #     self.find_element(*self.bbs_login_button_loc).click()

    # 设置定位元素类型及值
    login_username_loc = (By.ID, "j_username")
    login_password_loc = (By.ID, "j_password")
    login_button_loc = (By.ID, "j_login")

    # 登录用户名称
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 点击登录按钮
    def logon_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def user_login(self, username="1002", password='654321'):
        """获取的用户密码登录"""
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.logon_button()
        sleep(3)

    user_error_hint_loc = (By.XPATH, "html/body/form/div[2]/table[3]/tbody/tr/td/span")
    pawd_error_hint_loc = (By.XPATH, "html/body/form/div[2]/table[3]/tbody/tr/td/span")
    user_login_success_loc = (By.XPATH, "html/body/div[3]/div/div/div[3]/span[2]")

    # 用户名错误登录提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    # 用户密码错误登录提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

    # 登录成功
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
