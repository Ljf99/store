
'''
from appium import webdriver
url = '192.168.67.1:6666'
param = {
  "platformName": "Android",
  "platformVersion": "11",
  "deviceName": "192.168.67.1:6666",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": ".main.MainActivity"
}
driver = webdriver.Remote(url,param)
driver.find_element_by_xpath()
'''
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
#抖音
'''
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "11"
caps["deviceName"] = "192.168.67.1:6666"
caps["appPackage"] = "com.ss.android.ugc.aweme"
caps["appActivity"] = ".main.MainActivity"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
while True:
    TouchAction(driver).press(x=474, y=1511).move_to(x=499, y=853).release().perform()
    time.sleep(15)
    # driver.quit()

'''





