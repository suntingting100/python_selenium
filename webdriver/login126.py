from selenium import webdriver
import time


driver = webdriver.Chrome()
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

# 定位输入账号
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("suntingting_100")
# 定为输入密码
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("tingting685868")

# 点击登录按钮
driver.find_element_by_id("dologin").click()

# driver.switch_to.default_content()   # 释放iframe



