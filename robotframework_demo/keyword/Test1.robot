*** Settings ***


*** Test Cases ***
test1
   ${str1}    Catenate    Hello    word
   ${str2}    Catenate    SEPARATOR=---    Hello    word
   ${str3}    Catenate    SEPARATOR=    Hello    word    !
