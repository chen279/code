import time
import traceback
from selenium  import webdriver
url='http://132.232.44.158:8080/ljindex'
driver=webdriver.Chrome(executable_path='F:\\Vscode   file\\study code\\dailywork\\chromedriver.exe')  #启动chrome.exe驱动插件driver
#注意Chrome中的c是大写
driver.get(url)              #打开网址
driver.maximize_window()    #打开的界面最大化,window没有s
#开始进行元素定位
e=driver.find_element_by_xpath('//*[@id="unlogin"]/div[2]/a')   # 通过元素定位该按钮                     需要点F12打开开发者工具，查看元素，进行定位。
e.click()                   #点击元素

time.sleep(2)

driver.find_element_by_id('username').send_keys('chenche119')
driver.find_element_by_id('phonenum').send_keys('13697934607')
driver.find_element_by_id('password').send_keys('a111222333')
driver.find_element_by_id('confirpw').send_keys('a111222333')
driver.find_element_by_id('emailnum').send_keys('1143194727@qq.com')
driver.find_element_by_id('userRegist').click()
time.sleep(2)
driver.switch_to.alert.accept()          #.accept()          #定位网页弹窗#driver.switch_to_alert()
#断言开始，这用于判断测试用例是否通过。
#print(driver.current_url)
try:
    assert driver.current_url =='http://132.232.44.158:8080/ljindex/html/login.html'
    print('注册成功')
except:
    traceback.print_exc()
    print('注册失败')