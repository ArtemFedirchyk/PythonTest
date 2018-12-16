*** Settings ***
Documentation    Suite description
Library  Selenium2Library
Library  robot_login_pages/DriverManager.py
Library  robot_login_pages/IssuePageRobot

*** Test Cases ***
Test title
    [Tags]    DEBUG
    Provided precondition
    When action
    Then check expectations

*** Keywords ***
Provided precondition
