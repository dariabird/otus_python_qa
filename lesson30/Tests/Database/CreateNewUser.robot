*** Settings ***
Resource  ../../PageObjects/AdminPage.robot
Resource    ../../Resources/UserDataBase.robot

Suite Setup  Connect To Database  pymysql  ${DBName}  ${DBUser}  ${DBPass}  ${DBHost}  ${DBPort}
Suite Teardown  Disconnect From Database

Test Setup  Open Admin Page    ${BASE_URL}  ${BROWSER}
Test Teardown  Close Browser


*** Variables ***
${BROWSER}  chrome
${BASE_URL}  localhost:80
@{OPENCART_ADMIN} =  user  bitnami
${DBName}  bitnami_opencart
${DBUser}  bn_opencart
${DBPass}
${DBHost}  127.0.0.1
${DBPort}  3306
${TEST_USERNAME}    MyTestUsername


*** Test Cases ***
Add User With DB Validation
    [Documentation]  Add user to Users with ui and validate precence in database
    [Teardown]  Run Keywords  Execute Sql String  delete from ${USER_DB} where username = '${TEST_USERNAME}'
    ...  AND  Close Browser
    Delete User From Database    ${TEST_USERNAME}
    Login With    ${OPENCART_ADMIN}
    Add New User    ${TEST_USERNAME}
    Wait Until Keyword Succeeds  3 sec  1 sec  Check User In Database  ${TEST_USERNAME}
