from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化WebDriver
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com")

# 通过tag标签名定位元素，例如定位所有的<a>标签
elements = driver.find_elements(By.TAG_NAME, "a")

# 输出所有找到的<a>标签的文本内容
for element in elements:
    print(element.text)

# 关闭浏览器
driver.quit()