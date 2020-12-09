from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://reg.mail.163.com/unireg/call.do?cmd=register.entrance")

driver.find_element_by_id("nameIpt").send_keys("suntingting_100")
driver.find_element_by_id("mainPwdIpt").send_keys("tingting685868")
driver.find_element_by_id("mainCfmPwdIpt").send_keys("tingting685868")
driver.find_element_by_id("mainMobileIpt").send_keys("15510333822")
