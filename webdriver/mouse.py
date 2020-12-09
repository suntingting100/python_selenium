
from selenium.webdriver import ActionChains
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.maximize_window()

# 定位要悬停的元素 find_element_by_class_name("")
above = driver.find_element_by_xpath("//a[@id='s_usersetting_top']/span")

# 对定位的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()

time.sleep(1)

