
*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary


*** Test Cases ***
Open google.com
    Open Browser    chrome
    Go To url   https://google.com
