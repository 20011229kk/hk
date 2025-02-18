*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.baidu.com
${BROWSER}    Chrome

*** Test Cases ***
百度搜索梅西并跳转到详情页面
    打开浏览器并访问百度
    输入搜索内容并点击搜索按钮
    验证跳转到搜索结果页面
    等待搜索完成并关闭浏览器

*** Keywords ***
打开浏览器并访问百度
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

输入搜索内容并点击搜索按钮
    Wait Until Element Is Visible    id=kw    10s
    Input Text    id=kw    梅西
    Click Element    id=su    # 点击搜索按钮

验证跳转到搜索结果页面
    Wait Until Page Contains    梅西    10s
    Page Should Contain    梅西    # 页面应包含搜索词"梅西"

等待搜索完成并关闭浏览器
    Sleep    20s    # 等待20秒，确保搜索结果加载完毕
    Close Browser
