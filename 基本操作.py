from selenium import webdriver      #导入包
import time
driver = webdriver.Chrome()        #打开谷歌并赋值一个变量

#输入框练习
'''
driver.get(r"D:\Training\10.6\练习的html/frame.html")#打开网站地址
driver.maximize_window()    #最大化窗口
driver.find_element_by_xpath("//*[@id = 'input1']").send_keys('张刘生')
time.sleep(2)
driver.quit()
'''
'''
#弹窗练习
driver.get(r"D:/Training/10.6/练习的html/弹框的验证/dialogs.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id = 'alert' and @value = 'alert' and @type = 'button']").click()
# driver.switch_to.alert.accept()#点击确定
driver.switch_to.alert.dismiss()#点击取消
time.sleep(2)
driver.quit()
'''
'''
#文件上传及下拉框练习
driver.get(r"D:/Training/10.6/练习的html/上传文件和下拉列表/autotest.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@name = 'account' and @id = 'accountID' and @type = 'text']").send_keys("张刘生")
time.sleep(1)
driver.find_element_by_xpath("//*[@name = 'password' and @id = 'passwordID' and @type = 'password']").send_keys('admin')
time.sleep(1)
driver.find_element_by_xpath("//*[@id = 'areaID']").send_keys('北京市')
time.sleep(1)
driver.find_element_by_xpath("//*[@name = 'u2' and @id = 'sexID2' and @type = 'radio']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@name = 'u3' and @value = 'spring']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@name = 'u3' and @value = 'winter']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@name = 'file' and @type = 'file']").send_keys(r"D:\壁纸\4K公孙离.png")
time.sleep(2)
driver.quit()
'''
'''
#京东搜索操作练习

driver.get("https://www.jd.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@type= 'text' and @autocomplete= 'off' and @id='key' and @accesskey='s' and @class= 'text']").send_keys('电脑')
driver.find_element_by_xpath("//*[@class = 'button']").click()
time.sleep(15)#10秒左右，太短还没加载新页面就退出了
driver.quit()


# <input clstag="h|keycount|head|search_c" type="text" autocomplete='off' id="key" accesskey="s" class= 'text' aria-label="搜索" style="background: transparent;">
'''
'''
#必应搜索练习
driver.get("https://cn.bing.com/?scope=web&FORM=EDNTHT")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id = 'sb_form_q' and @class = 'sb_form_q' and @name = 'q' and @type = 'search']").send_keys('张刘生')
driver.find_element_by_xpath("//*[@stroke = '#007DAA']").click()
'''




















































































































