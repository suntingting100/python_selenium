from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.126.com")

# #浏览器最大化
driver.maximize_window()

# 休眠1s
time.sleep(1)

print("Before Login================")

# 打印当前title
title = driver.title
print(title)

# 打印当前url
now_url = driver.current_url
print(now_url)

# 执行邮箱登录
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

time.sleep(2)
print("After Login================")


# 再次打印当前页面title
title = driver.title
print(title)

# 打印当前页面url
now_url = driver.current_url
print(now_url)

# 获得登录用户名
user = driver.find_element_by_id("spnUid").text
print(user)


