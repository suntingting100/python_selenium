from selenium import webdriver
from time import sleep

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com")

try:
    driver.find_element_by_id("kw").send_keys("phantomjs")
    driver.find_element_by_id("su").click()
    sleep(1)
    driver.get_screenshot_as_file("D:\\baidu_ok.jpg")
except WebDriverException as msg:
    print(msg)
    driver.get_screenshot_as_file("D:\\baidu_error.jpg")
finally:
    driver.quit()