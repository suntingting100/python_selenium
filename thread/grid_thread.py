from threading import Thread
from selenium import webdriver
from time import sleep, ctime


# 测试用例
def test_baidu(host, browser):
    print("start:%s" % ctime())
    print(host, browser)
    dc = {"browserName": browser}
    driver = webdriver.Remote(command_executor=host,
                              desired_capabilities=dc)
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("browser")
    driver.find_element_by_id("su").click()
    driver.close()


if __name__ == "__main__":
    # 启动参数（指定运行机器与浏览器）
    lists = {"http://192.168.1.116:4444/wd/hub": "chorme",
             "http://192.168.1.116:5555/wd/hub": "internet explorer",
             "http://192.168.1.116:6666/wd/hub": "firefox" # 远程节点
              }

    threads = []
    files = range(len(lists))

    # 创建线程
    for host, browser in lists.items():
        t = Thread(target=test_baidu, args=(host, browser))
        threads.append(t)

    # 启动线程
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

    print("end:%s" % ctime())
