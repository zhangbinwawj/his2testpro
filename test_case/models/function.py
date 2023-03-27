from selenium import webdriver
import os


# 截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 获取项目的路径
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')  # 将'\'替换为：'/'
    base = base_dir.split('/test_case')[0]  # 项目路径，后面将截图存入该路径，split():截取
    file_path = base + "/reports/image/" + file_name  # 拼接截图的路径
    driver.get_screenshot_as_file(file_path)  # 获取错误的截图，并保存上面的路径里面


# if __name__ == '__name__':
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     insert_img(driver, 'baidu.jpg')
#     driver.quit()
