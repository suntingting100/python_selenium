from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
    """
    用户页面登录
    """
    url = "/"

    # Action    //*[@id="bbs-avatar"]/img
    bbs_login_user_loc = (By.XPATH, "//div['mzCust']/div/img")
    bbs_login_user_button = (By.ID, "mzlogin")

    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()
        sleep(1)
        self.find_element(*self.bbs_login_user_button).click()

    login_username_loc = (By.ID, "account")
    login_password_loc = (By.ID, "password")
    login_Button_Validation_loc = (By.LINK_TEXT, "点击按钮进行验证")
    login_button_loc = (By.ID, "login")

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 点击按钮验证
    def login_Button_Validation(self, button):
        self.find_element(*self.login_Button_Validation_loc).click()

    # 登录按钮
    def login_button(self, button):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def user_login(self, username="username", password="1111"):
        """获取的用户名密码登录"""
        self.open()
        self.bbs_login()
        self.login_username()
        self.login_password()
        self.login_Button_Validation()
        self.login_button()
        sleep(1)

    user_error_hint_loc = (By.XPATH, "//*[@id='mainForm']/div[2]/span[1]")
    pawd_error_hint_loc = (By.XPATH, "//*[@id='mainForm']/div[2]/span[1]")
    user_login_success_loc = (By.ID, "mzCustName")

    # 用户名提示错误
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    # 密码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

    # 登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text

