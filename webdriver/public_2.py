class Login2:
    # 登录 @staticmethod
    def user_login(self, driver, username, password):
        # 定位输入账号
        driver.find_element_by_name("email").send_keys(username)
        # 定为输入密码
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_id("dologin").click()
