from selenium import webdriver
import unittest
import time


class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.youdao.com"

    def test_youdao(self):
        """搜索关键词：webdriver"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys("webdriver")
        driver.find_element_by_link_text("翻译").click()
        # title = driver.title
        # self.assertEqual(title, "webdriver - 有道搜索")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
    