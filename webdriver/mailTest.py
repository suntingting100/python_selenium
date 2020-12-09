from selenium import webdriver
from public import Login
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.126.com")

# 浏览器最大化
driver.maximize_window()

# 休眠1s
time.sleep(1)

# 点击二维码至密码登录页
driver.find_element_by_id("lbNormal").click()

# 根据xpath定位ifram表单,切换iframe
iframe = driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
driver.switch_to.frame(iframe)

# 调用登录模块
Login().user_login(driver)

# 调用退出模块
Login().user_logout(driver)