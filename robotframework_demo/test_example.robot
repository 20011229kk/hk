*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}            https://console.easemob.com/user/login
${TITLE}          登录 - 环信即时通讯云
${USERNAME}       2939503115@qq.com
${PASSWORD}       258013kjl
${BROWSER}        chrome

*** Test Cases ***
Login And Verify Redirect
    # 打开浏览器并设置
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    20 seconds
    # 验证登录页面
    Title Should Be    ${TITLE}
    # 执行登录操作
    Wait Until Element Is Visible    id=username    timeout=10s
    Input Text    id=username    ${USERNAME}
    Input Text    id=password    ${PASSWORD}
    Click Button    xpath=//button[contains(@class, 'submit___3AGAq')]
    # 验证登录成功并跳转
    Sleep    5s    # 给跳转一些时间
    ${current_url}=    Get Location
    Log    Current URL: ${current_url}
    # 等待新页面加载
    Wait Until Location Contains    /index    timeout=20s
    Wait Until Page Contains Element    xpath=//div[contains(@class, 'header')]    timeout=20s
    # 截图验证
    Capture Page Screenshot    filename=login_success.png
    # 额外验证
    ${final_url}=    Get Location
    Log    Final URL: ${final_url}
    Should Be Equal    ${final_url}    https://console.easemob.com/index
    [Teardown]    Run Keywords    Capture Page Screenshot
    ...    AND    Close Browser
