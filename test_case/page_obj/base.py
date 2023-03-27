import time

class Page:
    """
    页面基础类，用于所有页面的继承，封装一些常用方法(逻辑层：用于存放一些封装好的功能用例模块)
    """

    def __init__(self, selenium_driver, parent=None):
        #self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    # 获取当前页面的url与设置url相比较
    # def on_page(self):
    #     return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        #url = self.base_url + url
        self.driver.get(url)
       # assert self.on_page(), 'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    # 定位元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 批量定位元素
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def script(self, src):
        return self.driver.execute_script(src)
