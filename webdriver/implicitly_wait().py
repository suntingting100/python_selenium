from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from time import ctime

driver = webdriver.Chrome()

# 设置隐式等待为10s
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys("selenium")
except NoSuchAttributeException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()

import time
inputs = driver.find_elements_by_tag_name("input")

for i in inputs:
    if i.get_attribute("type") == "checkbox":
        i.click()
        time.sleep(1)