*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Test Cases ***
List变量直接赋值
    @{list1}    Set Variable    1    2    3    4    5
    Set Global Variable    ${list1}
    Log    ${list1}
    @{list2}    Create List    6    7    8    9    10
    Log    ${list2}
追加值
    @{list3}    Create List    11    12    13    14    15
    Append To List    ${list3}    16
    Log    ${list3}
取值
    ${value}  Get From List    ${list1}    0
    Log    ${value}
    
