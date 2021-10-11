import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("还是喜欢")
driver.find_element_by_xpath("//*[@id='password']").send_keys("7418520")
driver.find_element_by_xpath("//*[@id='submit']").click()
#左侧列表隐藏
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/a[2]").click()
#左侧列表显示
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[2]/a").click()
time.sleep(2)
driver.quit()




























