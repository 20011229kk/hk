from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化WebDriver
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com")

# a = driver.current_url
# print(a)

# # 通过CSS选择器定位元素，例如定位搜索框
# element = driver.find_element(By.CSS_SELECTOR, '#kw')

# # 输出找到的搜索框的标签名
# print(element.tag_name)

# title = driver.title
# print(title)

# data = driver.page_source
# print(data)

window = driver.current_window_handle
print(window)
# 关闭浏览器
driver.quit()