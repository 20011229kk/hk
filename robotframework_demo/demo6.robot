*** Settings ***
Library           Collections

*** Test Cases ***
test1
    ${dict1}    Create Dictionary    name=Andy    age=20    gender=male
    Set Global Variable    ${dict1}
    Log    ${dict1}

获取所有的keys
    ${keys}    Get Dictionary Keys    ${dict1}
    Log    ${keys}

获取所有的values
    ${values}    Get Dictionary Values    ${dict1}
    Log    ${values}

根据key获取value
    ${value}    Get From Dictionary    ${dict1}    name
    Log    ${value}
