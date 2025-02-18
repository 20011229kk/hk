from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://release.easemob.com/#/login")

driver.find_element(By.NAME, "username").send_keys("kongjialin")
driver.find_element(By.NAME, "password").send_keys("202142060531Kjl")
driver.find_element(By.CLASS_NAME, "el-button").click()

# 增加等待时间，确保页面完全加载
sleep(10)

# 打印 localStorage 中的所有键值对
all_items = driver.execute_script("return window.localStorage;")
print("All localStorage items:", all_items)

# 尝试从 cookies 中获取 token
cookies = driver.get_cookies()
for cookie in cookies:
    if 'token' in cookie['name'].lower():
        print("Token:", cookie['value'])

driver.quit()