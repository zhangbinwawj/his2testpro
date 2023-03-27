# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.baidu.com/")

# get current url
print(driver.current_url)
print("打开百度成功")
