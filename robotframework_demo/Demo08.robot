*** Test Cases ***
For循环
    FOR    ${index}    ${english}    ${chinese}    IN
    ...    1    cat    猫
    ...    2    dog    狗
    ...    3    bird    鸟
        Log    ${index}.${english}-${chinese}
    END

For循环-range
    FOR    ${counter}    IN RANGE    1    11
        Log    ${counter}
    END
    FOR    ${counter1}    IN RANGE    5
        Log    ${counter1}
    END
    FOR    ${counter2}    IN RANGE    1    11    2
        Log    ${counter2}
    END
循环eixt-for-loop
    FOR    ${n}    IN    1    2    3    4    5
        Run Keyword If    ${n}==3    Exit For Loop
        Log    ${n}
    END