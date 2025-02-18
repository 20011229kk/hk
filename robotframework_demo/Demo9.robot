*** Settings ***
Library    BuiltIn

*** Test Cases ***
Evaluate Example
    ${result}    Evaluate    2 + 3
    Log    The result of 2 + 3 is ${result}

    ${list}    Evaluate    [1, 2, 3, 4, 5]
    Log    The list is ${list}

    ${uppercase}    Evaluate    "hello".upper()
    Log    Uppercase string is ${uppercase}

    ${sum}    Evaluate    sum([1, 2, 3, 4, 5])
    Log    The sum of the list is ${sum}