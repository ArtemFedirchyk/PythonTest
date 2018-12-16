*** Settings ***
Documentation  My Documentation
Library  Selenium2Library
Library  waiter_helper_robot.py
Library  LoginPageRobot.LoginPageRobot
Library  Abc


*** Variables ***
${Browser}  Chrome
${url}  http://localhost:8080
${username}  myName
${password}  myPassword

*** Keywords ***


*** Test Cases ***
My first suite
    my_function

#    Open Browser    ${url}  ${Browser}
#    login





