
from selenium import webdriver

driver = webdriver.Chrome()
# 参数数字为像素点
print("设置浏览器宽480、高800显示")
driver.maximize_window()

# 访问百度首页
first_url = "http://www.baidu.com"
print("now acess %s" % first_url)
driver.get(first_url)

# 访问新闻页面
second_url = "http://news.baidu.com"
print("now acess %s" % second_url)
driver.get(second_url)

# 返回/回退到百度首页
print("back to %s" % first_url)
driver.back()

# 前进到新闻页
print("forward to %s" % second_url)
driver.forward()

# 刷新页面
print("刷新页面")
driver.refresh()




