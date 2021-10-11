import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
#登陆
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("还是喜欢")
driver.find_element_by_xpath("//*[@id='password']").send_keys("7418520")
driver.find_element_by_xpath("//*[@id='submit']").click()
#退出
time.sleep(1)
driver.find_element_by_xpath("//*[@id='top']/div/a[2]/img").click()
time.sleep(1)
driver.quit()















