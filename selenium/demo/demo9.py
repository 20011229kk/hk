from selenium import webdriver
from selenium.common.exceptions import TimeoutException

# 初始化WebDriver
driver = webdriver.Chrome()

# 设置页面加载超时时间为10秒
driver.set_page_load_timeout(10)

try:
    # 打开百度首页
    driver.get("https://www.baidu.com")
    print("页面加载成功")
except TimeoutException:
    print("页面加载超时")

# 关闭浏览器
driver.quit()