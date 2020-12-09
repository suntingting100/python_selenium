from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("http://videojs.com/")

video = driver.find_element_by_class_name("vjs-tech")

# 返回播放文件地址  调用js方法同时javascript脚本
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

# 播放视频
print("start")
driver.execute_script("arguments[0].play()", video)

# 播放15s ]
sleep(15)

# 暂停视频
print("stop")
driver.execute_script("arguments[0].pause()", video)

driver.quit()




