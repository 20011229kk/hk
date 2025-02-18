from selenium import webdriver
from selenium.webdriver.common.by import By
# import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 初始化WebDriver
driver = webdriver.Chrome()

# 打开百度首页
driver.get("https://www.baidu.com")

# 硬性等待5秒
# time.sleep(5)
#隐式等待
# driver.implicitly_wait(5)



# 设置显示等待，等待搜索框元素出现，最长等待10秒
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#kkkk')))

# 输出找到的搜索框的标签名
# print(element.tag_name)

# 通过CSS选择器定位元素，例如定位搜索框
# element = driver.find_element(By.CSS_SELECTOR, '#kw')

# 输出找到的搜索框的标签名
# print(element.tag_name)




#查看元素是否已经加载出啦
wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.ID, "kw")))
 

# 关闭浏览器
driver.quit()