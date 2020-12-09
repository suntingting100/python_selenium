from selenium import webdriver
from public_2 import Login2


class LoginTest:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.126.com")
        self.driver.maximize_window()
        # 点击二维码至密码登录页
        self.driver.find_element_by_id("lbNormal").click()
        # 根据xpath定位ifram表单,切换iframe
        iframe = self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
        self.driver.switch_to.frame(iframe)

    # admin用户登录
    def test_admin_login(self):
        username = "suntingting_100"
        password = "tingting685868"
        Login2().user_login(self.driver, username, password)
        self.driver.quit()

    # guest 用户登录
    def test_guest_login(self):
        username = "guest"
        password = "123"
        Login2().user_login(self.driver, username, password)
        self.driver.quit()


LoginTest().test_admin_login()
LoginTest().test_guest_login()