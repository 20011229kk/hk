from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
sleep(3)
#刷新当前的界面
# driver.refresh()

#后退
# driver.back()
# sleep(3)

#前进
driver.forward()
sleep(3)
