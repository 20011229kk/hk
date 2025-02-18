from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 最大化浏览器窗口
# window_size = driver.maximize_window()

#获取窗口的位置
# window_position = driver.get_window_position()
# print(window_position)

#指定浏览器在左上角的位置
# driver.set_window_position(10,10)

#获取窗口的大小
# window_size = driver.get_window_size()
# print(window_size)

#设置浏览器窗口的大小
# driver.set_window_size(800,600)
sleep(3)
