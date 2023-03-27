from selenium.webdriver.common.by import By
from time import sleep

from test_case.page_obj.base import Page

"""注册挂号页面元素定位"""


class RegisterAction(Page):
    # 设置注册挂号页面元素定位类型及值
    registration_menu_button = (By.XPATH, "html/body/div[5]/div[2]/div/div[2]/div[1]/div[1]")
    register_menu_button = (By.XPATH, "html/body/div[5]/div[2]/div/div[2]/div[2]/div/li[1]/div/span[3]")
    register_button_loc = (By.XPATH, "html/body/div[2]/div/form/div/a[1]/span/span[1]")
    ifranme_xpath = (By.XPATH, "html/body/div[6]/div/div/div[2]/div[2]/div/iframe")

    # 切换注册挂号菜单
    def registration_menu(self):
        self.find_element(*self.registration_menu_button).click()

    # 挂号菜单
    def register_menu(self):
        self.find_element(*self.register_menu_button).click()

    # 挂号按钮
    def register_button(self):
        self.find_element(*self.register_button_loc).click()

    required_hint_box = (By.CSS_SELECTOR, ".tooltip-content")

    # 必填项为空提示
    def required_error_hint(self):
        return self.find_element(*self.required_hint_box).text

    # ifrance页面处理
    def ifranme(self):
        return self.find_element(*self.ifranme_xpath)
