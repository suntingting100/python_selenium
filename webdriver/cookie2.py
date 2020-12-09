from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.youdao.com")

# 向cookie的name 和 value中添加会话信息
driver.add_cookie({"name": "key-aaaaaa", "value": "value-bbbbbb"})

# 遍历cookies中的name和value信息并打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s : %s" % (cookie["name"], cookie["value"]))

driver.quit()