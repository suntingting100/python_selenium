from selenium.webdriver import Remote
import time

# 调用remote方法
driver = Remote(command_executor="http://192.168.1.116:4444/wd/hub",  # 10.3.237.75
                desired_capabilities={"browserName": "firefox",  # 浏览器 chorm,edge,ie,
                                      "version": "",            # 版本
                                      "platform": "ANY",        # 平台，ANY是当前平台 IOS,Android,
                                      "javascriptEnabled": True,  # 是否调用js

                                      # 此参数为firefox特有，是python客户端允许你远程控制基于gecko的浏览器或设备运行一个marionette设备
                                      "marionette": True}
                )

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("remote")
driver.find_element_by_id("su").click()

time.sleep(2)

driver.quit()
