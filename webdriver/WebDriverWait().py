# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_all_elements_located((By.ID, "kw")))
# element[0].send_keys("selenium")
#
from selenium import webdriver
from time import sleep, ctime

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

print(ctime())
for i in range(10):
    # noinspection PyBroadException
    try:
        el = driver.find_element_by_id("kw22")
        if el.is_displayed():
            break
        else:
            pass
            sleep(1)
    except:
        print("time out")
    driver.quit()
    print(ctime())

