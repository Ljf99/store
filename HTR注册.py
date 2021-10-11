import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver =webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("还是喜欢")
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys("习近平")
driver.find_element_by_xpath("//*[@id='pwd']").send_keys("7418520")
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys("7418520")
driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()
driver.find_element_by_xpath("//*[@id='valid_age']").send_keys("51")
driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]").send_keys("男")#男\女
driver.find_element_by_xpath("//*[@id='classname']").send_keys("测试开发")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys("999999@qq.com")
driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys("13111111111")
driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys("中南海")
driver.find_element_by_xpath("//*[@id='btn_reg']").click()
driver.find_element_by_xpath("/html/body/div[2]/div[3]/a/span/span").click()
time.sleep(2)
driver.quit()



















































































