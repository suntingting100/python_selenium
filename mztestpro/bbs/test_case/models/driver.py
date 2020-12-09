from selenium.webdriver import Remote
from selenium import webdriver


# 启动浏览器驱动
def browser():
    # 运行主机：端口号
    host = "192.168.1.116:4444"
    dc = {"browserName": "chrome"}  # 指定浏览器
    driver = Remote(command_executor="http://" + host + "/wd/hub",
                    desired_capabilities=dc)

    return driver


if __name__ == "__main__":
    dr = browser()
    dr.get("https://wwww.baidu.com")
    dr.quit()
