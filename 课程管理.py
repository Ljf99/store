import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
# 登陆教师端
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("caoshiming")
driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='submit']").click()
driver.find_element_by_xpath("//*[@id='_easyui_tree_13']/span[4]/a").click()
#添加课程
time.sleep(1)
driver.find_element_by_xpath("//*[@id='course_panel']/div/div/div[1]/table/tbody/tr/td/a/span/span[1]").click()
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[1]/td[2]/input").send_keys("拜佛")
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[2]/td[2]/textarea").send_keys("学会拜佛，永不宕机")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a[1]/span/span[1]").click()
#提示框确认
driver.find_element_by_xpath("/html/body/div[10]/div[3]/a/span/span").click()
#添加课程取消按钮
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a[2]/span/span[1]").click()
#关闭课程管理页面
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()
time.sleep(1)
driver.quit()

























