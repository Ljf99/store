'''
换头像
'''
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.find_element_by_xpath("//*[@id='img']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='ul_pic']/li[4]/img").click()  # 选择已有头像
time.sleep(2)
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()  # 关闭更换头像小窗口
time.sleep(2)
driver.quit()




