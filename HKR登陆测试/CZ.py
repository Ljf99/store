class loin:
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()

    def loginyes(self):
        return self.driver.title

    def loginerror(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text




