from selenium import webdriver

# 不用输验证码直接登录
# 访问xx网站
driver = webdriver.Chrome()
driver.get("http://www.xx.cn/")

# 将用户名写入浏览器cookie
driver.add_cookie({"name": "", "value": ""})
driver.add_cookie({"name": "", "value": ""})

# 再次访问网站时，将会自动登录
driver.get()