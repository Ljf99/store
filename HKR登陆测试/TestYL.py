from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from 自动化.day03.ceshi.CZ import loin
from 自动化.day03.ceshi.DL import InitPage
from selenium import webdriver
import time




@ddt
class Test1(TestCase):
    # 在所有方法执行前执行
    def setUp(self) -> None:

        self.driver = webdriver.Chrome()
        self.driver.get(r"http://localhost:8080/HKR")
        self.driver.maximize_window()

    # 在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()  # 退出浏览器

    @data(*InitPage.login_success_data)
    def testsuc(self,testdata):
        #获取数据类里的username
        username = testdata["username"]
        # 获取数据类里的password
        password = testdata["password"]
        # 获取数据类里的expect
        expect = testdata["expect"]
        #获取操作类的全局变量
        loinObj = loin(self.driver)
        # 将从数据类里获取到的username传给操作类里的username
        # 将从数据类里获取到的password传给操作类里的password
        loinObj.login(username,password)
        #获取实际结果
        data = loinObj.loginyes()
        #断言：判断实际结果与预期结果
        self.assertEqual(data,expect)

    @data(*InitPage.login_error_data)
    def testsuc1(self, testdata):
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        loinObj = loin(self.driver)
        loinObj.login(username, password)
        #获取结果
        data = loinObj.loginerror()
        #断言
        self.assertEqual(data, expect)


