*** Settings ***
Documentation    Login Tests
Library  Selenium2Library
Library  robot_login_pages/DriverManager.py
Library  robot_login_pages/LoginPageRobot.py
Library  robot_login_pages/WaiterHelper.py


*** Variables ***
${Browser}  Chrome
${url}  http://localhost:8080
${wrong_username}  myName
${wrong_password}  myPassword
${correct_username}  anastasia.fedirchyk
${correct_password}  Test1234
${login_page_url}  http://localhost:8080/login.jsp
${dashboard_page_url}  http://localhost:8080/secure/Dashboard.jspa

*** Test Cases ***
Wrong login
    ${driver} =    create driver
    first login  ${driver}   ${wrong_username}  ${wrong_password}
    assert url   ${driver}  ${login_page_url}
    close driver  ${driver}

Correct login
    ${driver} =    create driver
    first login  ${driver}   ${correct_username}   ${correct_password}
    assert url   ${driver}  ${dashboard_page_url}
    close driver  ${driver}



*** Keywords ***
Provided precondition
