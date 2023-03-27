from selenium import webdriver
from .driver import browser
import unittest
import os


class MyTest(unittest.TestCase):
    """定义mytest并基础单元测试框架的Testcase类
       用于用例的执行与结束执行步骤
    """

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)  # 设置隐式等待10S
        self.driver.maximize_window()  # 最大化当前浏览器窗口

    def tearDown(self):
        self.driver.quit()
