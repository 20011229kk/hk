from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化WebDriver
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com")

# 通过XPath定位元素，例如定位搜索框
element = driver.find_element(By.XPATH, '//*[@id="kw"]')

# 输出找到的搜索框的标签名
print(element.tag_name)

# 关闭浏览器
driver.quit()