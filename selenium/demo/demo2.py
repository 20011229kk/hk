from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 打开百度首页
driver.get("http://www.baidu.com")
# 最大化浏览器窗口
driver.maximize_window()
# 设置浏览器窗口位置
driver.set_window_position(400, 300)
# 设置浏览器窗口大小
driver.set_window_size(800, 600)
# 等待5秒
time.sleep(5)

# 通过class name定位搜索输入框元素并输入"messi"
driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("messi")
# 通过class name定位搜索按钮并点击
driver.find_element(By.CSS_SELECTOR, ".bg.s_btn").click()

# 等待3秒以便搜索结果加载
time.sleep(3)

# 关闭浏览器
driver.quit()