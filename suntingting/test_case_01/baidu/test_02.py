from selenium import webdriver
import unittest
import HTMLTestRunner
import time


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
        time.sleep(2)
        driver.find_element_by_id("su").click()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 定义报告存放路径
    filename = "D:\\python file location\\report\\" + now + " result.html"
    # wb是以二进制写模式打开当前目录下的文件。如果没有，则会自动创建文件
    fp = open(filename, "wb")

    # 定义测试报告  调用HTMLTestRunner模块下的HTMLTestRunner类
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="百度搜索测试用例",
                                           description="用例执行情况")
    print(runner)

    runner.run(testunit)   # 运行测试用例 HTMLTestRunner下的run()方法运行测试套件中组装的测试用例
    fp.close()  # 关闭报告文件
