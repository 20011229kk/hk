from selenium import webdriver
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

alert = driver.switch_to.alert

#获取弹窗的文本内容
alert_text = alert.text
print(alert_text)

#点击弹窗的确定按钮
alert.accept()
#点击弹窗的取消按钮
#alert.dismiss()
#输入内容
#alert.send_keys("hello")