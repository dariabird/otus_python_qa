*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${LOGIN_FORM}  css=form
${USERNAME_INPUT}  css=#input-username
${PASSWORD_INPUT}  css=#input-password
${SUBMIT_BUTTON}  css=button[type='submit']
${LOGOUT_BUTTON}    css=.navbar-nav>li:nth-child(2)
${MENU_SYSTEM}  css=#menu-system
${CATALOG_ITEMS}  css=#collapse7 > li > a
${USERS_MENU_ITEM}  css=#collapse7-1 > li > a
${ADD_USER_BUTTON}  xpath=//a[@data-original-title='Add New']
${SAVE_USER_BUTTON}    xpath=//button[@data-original-title='Save']
${USERNAME_INPUT}   css=[name=username]
${FIRST_NAME_INPUT}  css=[name=firstname]
${LAST_NAME_INPUT}    css=[name=lastname]
${EMAIL_INPUT}    css=[name=email]
${PASSWORD_INPUT}    css=[name=password]
${PASSWORD_CONFIRM_INPUT}    css=[name=confirm]


*** Keywords ***
Open Admin Page
    [Arguments]     ${BASE_URL}  ${BROWSER}
    Open Browser  url=http://${BASE_URL}/admin/  browser=${BROWSER}  options=add_argument("--ignore-certificate-errors");add_argument("--start-maximized")

Login With
    [Arguments]  ${user_data}
    Wait Until Element Is Visible  ${LOGIN_FORM}
    Input Text  ${USERNAME_INPUT}  ${user_data}[0]
    Input Text  ${PASSWORD_INPUT}  ${user_data}[1]
    Submit Form  ${LOGIN_FORM}

Check Logout Button Present
    Wait Until Element Is Visible    ${LOGOUT_BUTTON}

Click Logout
    Click Element    ${LOGOUT_BUTTON}

Check We Are On Login Page
    Wait Until Element Is Visible   ${USERNAME_INPUT}
    Wait Until Element Is Visible   ${PASSWORD_INPUT}

Open System Users Catalog
    Click Element  ${MENU_SYSTEM}
    ${catalog_items} =  Get Webelements  ${CATALOG_ITEMS}
    BuiltIn.Wait Until Keyword Succeeds  3 sec  1 sec  Click Element  ${catalog_items}[1]
    ${system_items} =    Get Webelements  ${USERS_MENU_ITEM}
    BuiltIn.Wait Until Keyword Succeeds  3 sec  1 sec  Click Element  ${system_items}[0]
    Wait Until Page Contains Element  xpath=//h1[text()='Users']

Add New User
    [Arguments]  ${username}    ${first_name}=Test    ${last_name}=Test    ${email}=test@test.com   ${password}=12345678
    Open System Users Catalog
    Click Element    ${ADD_USER_BUTTON}
    Input Text    ${USERNAME_INPUT}    ${username}
    Input Text    ${first_name_input}    ${first_name}
    Input Text    ${last_name_input}    ${last_name}
    Input Text    ${email_input}    ${email}
    Input Text    ${password_input}    ${password}
    Input Text    ${password_confirm_input}    ${password}
    Click Element    ${SAVE_USER_BUTTON}

