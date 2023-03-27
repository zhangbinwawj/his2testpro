from selenium.webdriver import Remote
from selenium import webdriver
from time import sleep
"""
定义驱动文件
"""


# 启动浏览器驱动
def browser():
    # driver = webdriver.Chrome()
    host = '127.0.0.1:4444'  # 运行主机：端口号
    dc = {'platform': 'ANY',
          'browserName': 'chrome',  # 指定浏览器
          'version': '',
          'javascriptEnabled': True
          }
    driver = Remote(command_executor='http://' + host + '/wd/hub',
                    desired_capabilities=dc)
    return driver


# if __name__ == '__main__':
#     dr = browser()
#     dr.get("https://www.baidu.com")
#     sleep(10)
#     dr.quit()
