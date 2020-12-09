from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os


# ============定义发送邮件===========
def send_mail(file_new):
    f = open(file_new, "rb")
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, "html", "utf-8")
    msg["subject"] = Header("自动化测试报告", "utf-8")
    msg["from"] = "suntingting_100"
    msg["to"] = "617587058@qq.com"

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("suntingting_100@126.com", "123456a")
    smtp.sendmail("suntingting_100@126.com", "617587058@qq.com", msg.as_string())
    smtp.quit()
    print("email has send out")


# =========查找测试包裹目录，找到最新生成的测试报告文件=======
def new_report(testreport):
    # testreport = "D:\\python file location\\report\\"
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == "__main__":

    test_dir = "D:\\python file location\\suntingting\\test_case_02\\"
    test_report = "D:\\python file location\\report\\"

    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern="test_*.py")
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + "\\" + now + "result.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp,
                            title="测试报告111",
                            description="用例执行情况")
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)
