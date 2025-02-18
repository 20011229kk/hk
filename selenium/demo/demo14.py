from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

#模拟鼠标右键点击
# driver.find_element(By.ID, "kw").send_keys("messi")
# driver.find_element(By.ID, "su").click()
# sleep(3)

#模拟鼠标悬停
# mouse = driver.find_element(By.LINK_TEXT, "设置")
# driver.move_to_element(mouse).perform()
# sleep(3)

#鼠标双击
# double_click_element = driver.find_element(By.ID, "kw")
# actions = ActionChains(driver)
# actions.double_click(double_click_element).perform()

#鼠标拖拽
# source_element = driver.find_element(By.ID, "kw")
# target_element = driver.find_element(By.ID, "su")
# actions = ActionChains(driver)
# actions.drag_and_drop(source_element, target_element).perform()

#鼠标移动到指定元素
mouse = driver.find_element(By.LINK_TEXT, "设置")
actions = ActionChains(driver)
actions.move_to_element(mouse).perform()
