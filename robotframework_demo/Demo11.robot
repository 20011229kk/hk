*** Settings ***
Library    SeleniumLibrary
*** Keywords ***
Do Something
    [Arguments]    ${arg1}    ${arg2}    ${arg3}    ${arg4}    ${arg5}    ${arg6}    ${arg7}    ${arg8}    ${arg9}    ${arg10}
    Log    ${arg1} ${arg2} ${arg3} ${arg4} ${arg5} ${arg6} ${arg7} ${arg8} ${arg9} ${arg10}
*** Test Cases ***
#行续延
Example Of Line Continuation
    [Documentation]    This is a test case for line continuation...
    ...    long lists of arguments or other long lines of code.
    Do Something    argument1    argument2    argument3    argument4    argument5...
    ...    argument6    argument7    argument8    argument9    argument10
    

        