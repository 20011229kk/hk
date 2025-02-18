
*** Settings **


*** Test Cases ***
test1
    ${var}    Set Variable    a    b    c
    Log Many    ${var}

    FOR    ${n}    IN    @{var}
        Log    ${n}
    END
    