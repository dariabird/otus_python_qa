*** Settings ***
Resource  ../../PageObjects/MainPage.robot
Test Setup  Open Main Page    ${BASE_URL}  ${BROWSER}
Test Teardown  Close Browser


*** Variables ***
${BROWSER}  chrome
${BASE_URL}  localhost:80


*** Test Cases ***
Test Brand Carouse Present On Page
    [Documentation]    Tests brand carousel is on the main page
    Check Brand Carousel Present