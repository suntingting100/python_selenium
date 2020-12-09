from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Page(object):
    """
    基础类，用于页面对象类的继承
    """

    login_url = "http://www.126.com"

    # 初始化——init_方法
    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url  # 定义基本的URL（base_url）
        # 要引用driver，但是这里还未定义具体的浏览器，所以用self.driver代替
        self.driver = selenium_driver   # 定义驱动(driver)
        self.timeout = 30  # 定义超时时间（timeout）

    # url地址的断言部分，交由 on_page()方法来实现
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    # __open()表示类内部的私有函数方法，不供外部调用
    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), "Did not land on %s" % url

    # 定义open()方法打开url网站，但他本身并未做这件事么认识交给_open()方法
    def open(self):
        self._open(self.url)

    # 元素定位方法封装
    def find_element(self, *loc):
        return self.driver.find_element(*loc)


# LoginPage()类中主要对登陆页面上的元素进行封装，使其成为更具体的操作方法，例如,用户名、密码和登陆按钮都被封装成了方法
class LoginPage(Page):
    """
    126邮箱登陆页面模型
    """
    url = "/"

    # 定位器
    username_loc = (By.ID, "idInput")
    password_loc = (By.ID, "pwdInput")
    submit_loc = (By.ID, "LoginBtn")  #  submit提交的意思

    # Action
    def type_username(self, username):
        # 调用父类的方法find_element，相当于是在同一个类中，遵从同一个类中调用方法格式：self.方法名()
        # *self.username_loc调用变量要用self初始化，否则类函数无法调用类变量
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()

# test_user_login()函数将单个的元素操作组成一个完整的动作，这个动作包含了打开浏览器，输入用户名/密码，点击登陆等单步步骤
# 在使用该函数时，需要将driver,username,password等信息作为函数的入参
def test_user_login(driver, username, password):
    """测试获取的用户名/密码是否可以登陆"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()


def main():
    try:
        driver = webdriver.Firefox()
        username = "username"
        password = "123456"
        test_user_login(driver, username, password)
        sleep(3)
        text = driver.find_element_by_id("spnUid").text
        assert (text == "username@126.com"), "用户名不匹配，登陆失败！"

    finally:
        # 关闭浏览器窗口
        driver.close()

if __name__ == "main":
    main()



