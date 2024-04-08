*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${arg_name}     https://google.com

*** Test Cases ***
Test Case 1
    Open Browser     ${arg_name}
