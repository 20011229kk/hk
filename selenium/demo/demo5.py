from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化WebDriver
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com")

# 通过partial link text定位元素，例如定位包含“闻”的链接
element = driver.find_element(By.PARTIAL_LINK_TEXT, "闻")

# 输出找到的链接的文本内容
print(element.text)

# 关闭浏览器
driver.quit()