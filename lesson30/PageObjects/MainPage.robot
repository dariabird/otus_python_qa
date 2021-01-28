*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${BRANDS_CAROUSEL}  css=div#carousel0


*** Keywords ***
Open Main Page
    [Arguments]     ${BASE_URL}  ${BROWSER}
    Open Browser  url=http://${BASE_URL}  browser=${BROWSER}    options=add_argument("--ignore-certificate-errors");add_argument("--start-maximized")

Check Brand Carousel Present
    Wait Until Element Is Visible    ${BRANDS_CAROUSEL}



