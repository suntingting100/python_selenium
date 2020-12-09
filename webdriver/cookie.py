from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.youdao.com")

# 获得cookie信息
cookie = driver.get_cookies()

# 讲获得的cookie信息打印
print(cookie)
