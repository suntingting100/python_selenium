from selenium import webdriver
import unittest
from HtmlTestRunner import HTMLTestRunner
import sys


class Baidu(unittest.TestCase):
    """百度搜索测试"""
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"

    def test_baidu_search(self):
        """搜索关键字"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    # 定义报告存放路径
    filename = "D:\\python file location\\report\\result.html"
    fp = open(filename, "w")  # 此时要用w,wb是打开二进制文件，会报错

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, report_title="百度搜索测试报告")
    runner.run(testunit)   # 运行测试用例
    fp.close()  # 关闭报告文