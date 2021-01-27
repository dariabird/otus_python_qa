*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${LOGIN_FORM}  css=form
${USERNAME_INPUT}  css=#input-username
${PASSWORD_INPUT}  css=#input-password
${SUBMIT_BUTTON}  css=button[type='submit']
${LOGOUT_BUTTON}    css=.navbar-nav>li:nth-child(2)


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

