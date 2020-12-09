from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest  # 引入unittest框架
import time
import HtmlTestRunner


class BaiduTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []  # 定义空的verificationErrors数组，脚本运行时的错误信息将被记录在这个数组中
        self.accept_next_alert = True  # 定义accept_next_alert变量，表示是否接受下一个警告，初始状态为True

    def test_baidu(self):   # test_baidu中放置的是我们的测试脚本
        driver = self.driver
        driver.get(self.base_url + "/")  # 加/ 是为了访问他的下一级节点
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys("selenium ide")
        driver.find_element_by_id("su").click()
        time.sleep(2)

    def is_element_present(self, how, what):   # is_element_present方法用于查找页面元素是否存在
        try:
            self.driver.find_element(by=how, value=what)  # find_element（）来接收元素的定位方法how 和定位值 what
        except NoSuchElementException as e:
            return False  # except是python异常处理，否则则抛出异常并返回False
        return True  # 若定位到返回

    def is_alert_present(self):  # is_alert_present（）方法用于判断当前页面是否有警告框
        try:
            self.driver.switch_to.alert()   # wendriver提供的switch_to.alert()方法捕捉页面上的警告框
        except NoAlertPresentException as e:
            return False   # 没有捕捉到,抛出异常并返回False
        return True   # 捕捉到返回True

    def close_alert_and_get_its_text(self):  # 关闭警告并获得警告信息
        try:
            alert = self.driver.switch_to.alert()  # 获得警告
            alert_text = alert.text  # 获得警告框信息
            if self.accept_next_alert:  # 如果accept_next_alert状态为True
                alert.accept()  # 则接受警告
            else:
                alert.dismiss()  # 否则就忽略
        finally:
            self.accept_next_alert = True

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
        # 通过assertEqual（）比较其是否为空，如果为空则说明执行用例过程中没有出现异常，否则则抛出异常
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
