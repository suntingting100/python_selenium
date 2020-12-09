
# window.scrollTO(左边距，上边距)
# window.scrollTO(0,450)

from selenium import webdriver
from time import sleep

# 访问百度
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 设置浏览器大小
driver.set_window_size(600, 600)

# 搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 通过javascript设置浏览器窗口的滚动条位置   js代码
js = "window.scrollTo(100,450);"

# execute_script 执行js代码
driver.execute_script(js)
sleep(3)

driver.quit()