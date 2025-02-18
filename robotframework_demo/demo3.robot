*** Settings ***
Library    SeleniumLibrary
Library    DateTime
Library    Collections

*** Variables ***
@{initial_list}    1    2    3    4    5    # 静态列表定义

*** Test Cases ***
test1
    # 获取时间
    ${current_time}=    Get Time
    Log    Current time is: ${current_time}
Get赋值
    # 创建列表
    ${list}=    Create List    1    2    3    4    5
    Log    List contents: ${list}

    # 获取列表长度
    ${length}=    Get Length    ${list}
    Log    List length is: ${length}
test3
    # 打印静态列表内容
    Log    ${initial_list}
    
    # 获取静态列表长度
    ${static_length}=    Get Length    ${initial_list}
    Log To Console   Static list length is: ${static_length}