from selenium import selenium

sel = selenium("localhost", "4444", "*firefox", "http://www.baidu.com")

sel.start()

sel.open("/")

sel.type("id=kw", "selenium grid")
sel.click()
