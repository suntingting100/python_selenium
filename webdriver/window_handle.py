from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
search_window = driver.current_window_handle

driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("立即注册").click()

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != search_window:
        driver.switch_to.window(handle)
        print("now register window")
        driver.find_element_by_name("userName").send_keys("userName")
        driver.find_element_by_name("phone").send_keys("15510333822")
        time.sleep(2)

# 回到搜索窗口
for handle in all_handles:
    if handle == search_window:
        driver.switch_to.window(handle)
        print("now search window")
        driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)

driver.quit()