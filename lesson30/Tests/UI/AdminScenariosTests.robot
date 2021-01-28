*** Settings ***
Resource  ../../PageObjects/AdminPage.robot
Test Setup  Open Admin Page    ${BASE_URL}  ${BROWSER}
Test Teardown  Close Browser

*** Variables ***
${BROWSER}  chrome
${BASE_URL}  localhost:80
@{OPENCART_ADMIN} =  user  bitnami

*** Test Cases ***
Test Admin Login And Quit
    [Documentation]    Tests that admin logs in and then quits
    Login With    ${OPENCART_ADMIN}
    Check Logout Button Present
    Click Logout
    Check We Are On Login Page


