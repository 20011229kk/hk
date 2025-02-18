from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# select下拉框对应的操作
driver = webdriver.Chrome()
driver.get("https://2345.com/")
# 定位select下拉框
select = driver.find_element(By.CLASS_NAME, "select-province")
# 获取select下拉框的所有选项
options = select.find_elements(By.TAG_NAME, "option")
# 遍历所有选项
for option in options:
    # 输出选项的值和文本
    print(option.get_attribute("value"), option.text)
# 选中第二个选项
options[1].click()
# 关闭浏览器 
driver.quit()