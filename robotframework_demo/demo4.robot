*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${number1}    1

*** Test Cases ***
作用域
    Log    ${number1}
    ${number2}=    Set Variable    2     #Set  Variable 设置变量,通常用于Test Case中
    Set Suite Variable    ${number2}    #Set Suite Variable 设置套件变量 可以在别的test case中使用
    # Set Global Variable    ${number2}    #Set Global Variable 设置全局变量 可以在别的test case中使用
    Log    ${number2}
test2
    Log    ${number2}
    


