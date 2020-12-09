from selenium.webdriver import Remote
import time

# 定义主机和浏览器
lists = {"http://192.168.1.116:4444/wd/hub": "chrome",
         "http://192.168.1.116:5555/wd/hub": "firefox"}
         # "http://192.168.1.116:5556/wd/hub": "internet explorer"

# 通过不同的浏览器执行脚本
for host, browser in lists.items():  # items() 函数作用：以列表返回可遍历的(键, 值) 元组数组。
    print(host, browser)

    driver = Remote(command_executor=host,
                    desired_capabilities={"browserName": browser,
                                          "version": "",
                                          "platform": "ANY",
                                          "javascriptEnable": True
                                          }
                    )

    driver.get("http://wwww.baidu.com")
    driver.find_element_by_id("kw").send_keys(browser)
    driver.find_element_by_id("su").click()
    time.sleep(1)

    driver.quit()