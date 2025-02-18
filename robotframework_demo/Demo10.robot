*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
test1
    Open Browser    https://www.baidu.com    chrome
    # 等待元素包含指定的文本
    Wait Until Element Contains    link=新闻    新闻    5s
    # 等待元素可用
    Wait Until Element Is Visible    link=新闻    5s
    # 等待页面包含指定的文本
    Wait Until Page Contains    百度一下    5s
    # 等待页面包含指定的元素
    Wait Until Page Contains Element    id=kw    5s
    Close Browser

