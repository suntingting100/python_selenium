
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

time.sleep(1)

driver.find_element_by_id("translateContent").send_keys("hello")
time.sleep(1)
# 提交输入框内容
driver.find_element_by_id("translateContent").submit()



