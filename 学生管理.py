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
#学生管理
driver.find_element_by_xpath("//*[@id='_easyui_tree_12']").click()
#姓名查询框输入
time.sleep(1)
driver.find_element_by_xpath("//*[@id='J-stu']").send_keys("习")
#点击查询
driver.find_element_by_xpath("//*[@id='stu_panel']/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]").click()
'''
#电话查询输入框
time.sleep(1)
driver.find_element_by_xpath("//*[@id='J-phone']").send_keys("1")
#点击查询
driver.find_element_by_xpath("//*[@id='stu_panel']/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]").click()
'''
#切换毕业/未毕业
driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[11]/div/a").click()
time.sleep(2)
#点击提示框的确认
driver.find_element_by_xpath("/html/body/div[8]/div[3]/a/span/span").click()
time.sleep(1)
#关闭学生管理页面
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()
time.sleep(1)
#关闭浏览器
driver.quit()





























