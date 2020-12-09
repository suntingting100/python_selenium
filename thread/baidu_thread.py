from threading import Thread
from selenium import webdriver
from time import ctime, sleep


# 测试用例
def test_baidu(browser, search):
    print("Start:%s" % ctime())
    print("browser:%s" % browser)
    if browser == "ie":
        driver = webdriver.Ie()
    elif browser == "chorme":
        driver = webdriver.Chrome()
    elif browser == "ff":
        driver = webdriver.Firefox()
    else:
        print("browser参数有误，只能为ie、ff、chorme")

    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("search")
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()


if __name__ == "__main__":
    # 启动参数（指定浏览器与搜索的内容）
    lists = {"chorme": "threading", "ie": "webdriver", "ff": "python"}

    threads = []
    files = range(len(lists))   # range(3)

    # 创建线程
    for browser, search in lists.items():
        t = Thread(target=test_baidu, args=(browser, search))
        threads.append(t)

    # 启动线程
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()

    print("end:%s" % ctime())
    