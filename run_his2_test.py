from package.HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os


# =====================定义发送邮件=====================
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # mail_body:文本内容，html：文本格式，设置编码
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['From'] = Header("自动化报告", 'utf-8')  # 发送者
    msg['To'] = Header("张斌", 'utf-8')  # 接收者
    # 邮件主题
    subject = 'HIS自动化测试'
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    # 发件人的邮箱及密码
    smtp.login("zhangbinwawj@163.com", "wawj6969130")
    # 发件人、收件人账号，最后发送邮件
    smtp.sendmail("zhangbinwawj@163.com", "zhangbinwawj@163.com", msg.as_string())
    smtp.quit()
    print("email has send out !")


# 查找测试报告目录，找到最新的生成测试报告
def new_report(testreport):
    lists = os.listdir(testreport)  # 列举test_dir目录下的所有文件（名），结果以列表形式返回。
    # sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = 'D:/his2testpro/reports/' + now + '_测试报告.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,  # 报告文件名称
                            title='HIS系统自动化测试报告',  # 测试报告的名称
                            description='环境：windows 浏览器：Chrome')
    # 调用test_case文件夹下_sta.py文件
    discover = unittest.defaultTestLoader.discover('D:/his2testpro/test_case',
                                                   pattern='*_sta.py')
    runner.run(discover)  # 运行测试用例
    fp.close()  # 关闭生成的报告
    file_path = new_report('D:/his2testpro/reports/')  # 查找生成的报告
    send_mail(file_path)  # 调用发邮件的模块
