*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${arg_name0}     https://google.com
${arg_name1}     https://google.com

*** Test Cases ***
Test Case 1
    Open Browser     ${arg_name0}
    Go To     ${arg_name1}
