*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${boyname}    Andy    # 第一种方式：直接赋值
${girlname}    Lucy
*** Test Cases ***

Set赋值
    # 第一种方式：直接赋值的使用
    # Log    Boy name is: ${boyname}
    # Log    Girl name is: ${girlname}
    
    # 第二种方式：条件判断后赋值
    ${a}=    Set Variable    2
    ${b}=    Set Variable    3
    
    ${girlname}=    Run Keyword If    '${a}'=='${b}'    Set Variable    Andy
    ...    ELSE    Set Variable    Lucy
    
    Log    Girl name is: ${girlname}    
