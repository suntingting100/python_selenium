class Login():

    # 登录
    def user_login(self, driver):
        # 定位输入账号
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("suntingting_100")
        # 定为输入密码
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("tingting685868")
        driver.find_element_by_id("dologin").click()

    # 退出
    def user_logout(self, driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()