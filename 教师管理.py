import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
#登陆教师端
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("caoshiming")
driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='submit']").click()
#教师管理
driver.find_element_by_xpath("//*[@id='_easyui_tree_11']").click()
#教师姓名查询框
time.sleep(1)
driver.find_element_by_xpath("//*[@id='sear_teaname']").send_keys("贾")
#点击查询
driver.find_element_by_xpath("//*[@id='search_user']/span/span[2]").click()
#点击重置密码
driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[9]/div/a").click()
time.sleep(1)
#点击提示框的确定
driver.switch_to.alert.accept()


















































