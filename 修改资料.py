import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("还是喜欢")
driver.find_element_by_xpath("//*[@id='password']").send_keys("7418520")
driver.find_element_by_xpath("//*[@id='submit']").click()
#修改个人信息
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']/span[4]/a").click()
#修改用户名
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[1]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[1]/td[2]/input").send_keys("还是喜欢")
#修改密码
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[3]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[3]/td[2]/input").send_keys("7418520")
#修改年龄
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").clear()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").send_keys('51')
#修改性别
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[5]/td[2]/select").send_keys("男")
#修改地址
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").send_keys("中南海")
#修改邮箱
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[8]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[8]/td[2]/input").send_keys("999999@qq.com")
#个性名片
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[9]/td[2]/textarea").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[9]/td[2]/textarea").send_keys("我要打十个")
#提交修改
driver.find_element_by_xpath("//*[@id='btn_modify']").click()
time.sleep(1)
#关闭页面
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()
time.sleep(1)
#关闭浏览器
driver.quit()










































