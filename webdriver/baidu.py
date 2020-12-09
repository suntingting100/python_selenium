from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# 获得输入框的尺寸
size = driver.find_element_by_id("kw").size
print(size)

# 返回页面底部备案信息//*[@id="bottom_container"]/div/div[2]/div[1]/span/span[2]
text = driver.find_element_by_xpath("(//span[@class='copyright-text']/span)[2]").text
# print(text)

# 返回元素的属性值，可以是id，name,type或任意属性
attribute = driver.find_element_by_id("kw").get_attribute("type")
print(attribute)

# 返回元素的结果是否课件，返回结果为True或False
result = driver.find_element_by_id("kw").is_displayed()
print(result)

# 输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")

# 删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 输入空格键+ “教程”
driver.find_element_by_id("kw").send_keys("Keys.SPACE")
driver.find_element_by_id("kw").send_keys("教程")

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

# 通过回车键来代替单机操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)

driver.quit()