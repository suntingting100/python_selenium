from selenium import webdriver
import os,time

# 创建Chrome浏览器配置对象实例
chromeOptions = webdriver.ChromeOptions()

# profile.default_content_settings.popups：0 为屏蔽弹窗，1 为开启弹窗
# download.default_directory：指定路径
# os.getcwd() ：返回当前进程的工作目录
# 禁止加载图片

prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': os.getcwd(),
         'profile.default_content_setting_values': {'images': 2}
         }

chromeOptions.add_experimental_option('prefs', prefs)

# 启动参数要写在下方句代码前面
driver = webdriver.Chrome(options=chromeOptions)

driver.get("https://pypi.org/project/selenium/#files")
driver.maximize_window()
driver.find_element_by_partial_link_text("selenium-3.141.0-py2.py3-none-any.whl").click()

time.sleep(2)