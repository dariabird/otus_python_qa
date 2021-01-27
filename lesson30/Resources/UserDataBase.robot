*** Settings ***
Library  DatabaseLibrary


*** Variables ***
${USER_DB}  oc_user


*** Keywords ***
Check User In Database
    [Arguments]  ${username}
    Check If Exists In Database  select username from ${USER_DB} where username = '${username}'

Check User Not In Database
    [Arguments]  ${username}
    Check If Not Exists In Database  select username from ${USER_DB} where username = '${username}'

Delete User From Database
    [Arguments]  ${username}
    Execute Sql String  delete from ${USER_DB} where username = '${username}'