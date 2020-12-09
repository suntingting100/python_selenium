from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.baidu.com")

# 鼠标悬停至“设置”链接
link = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()

# 打开搜索设置
driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)

# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)

# 接受警告框
driver.switch_to.alert.accept()

# 拒绝警告框  driver.switch_to.alert.dismiss()
# 如果alert弹框上有文本框，可以输入文字  driver.switch_to.alert.sendkeys()
# 返回alert上的文本内容 text = driver.switch_to.alert.text

# driver.quit()