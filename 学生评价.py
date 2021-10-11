import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("还是喜欢")
driver.find_element_by_xpath("//*[@id='password']").send_keys("7418520")
driver.find_element_by_xpath("//*[@id='submit']").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select").send_keys("9")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select").send_keys("7")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select").send_keys("9")
driver.find_element_by_xpath("//*[@id='tea_td']/select").send_keys("贾")
#	本次学习都理解了么
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[5]/td[3]/div/label[4]/div").click()
#对工作帮助大么？
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[6]/td[2]/div/label[3]/div").click()
#符合实际企业需要
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[7]/td[3]/div/label[3]/div").click()
#语言、思路清晰明确
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[8]/td[2]/div/label[3]/div").click()
#针对性、系统性强
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[9]/td[2]/div/label[3]/div").click()
#以后有机会还愿意来学么？
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[10]/td[3]/div/label[3]/div").click()
#本次学习还满意吗
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[3]/div").click()
#达到学习目的了么？
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[12]/td[2]/div/label[2]/div").click()
#评价
driver.find_element_by_xpath("//*[@id='textarea']").send_keys("拜托，你很弱诶")
#提交
driver.find_element_by_xpath("//*[@id='subtn']").click()
#弹窗    /html/body/div[7]/div[3]/a/span/span
# driver.find_element_by_xpath("/html/body/div[7]/div[3]/a/span/span").click()
#二次提交弹窗
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a/span/span").click()
#关闭浏览器
driver.quit()




















