from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

# 截取当前窗口 并指定截图图片的保存位置  注意：png格式
driver.get_screenshot_as_file("D://pyse\\baidu_img.png")

driver.quit()