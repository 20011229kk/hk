from selenium import webdriver
from selenium.webdriver.common.by import By

dirver = webdriver.Chrome()
dirver.get("https://www.baidu.com")

element = dirver.find_element(By.LINK_TEXT, "hao123")
print(element.text)
dirver.quit()