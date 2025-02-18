*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
f1
    [Arguments]    ${a}    ${b}
    ${result}    Evaluate    ${a}+${b}  
    Log    ${result}

*** Variables ***
# 定义变量
${str}    30

*** Test Cases ***
test1
    f1    3    4
    ${time}    Get Time
    Log    ${time}