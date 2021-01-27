*** Settings ***
Resource  ../../PageObjects/ProductPage.robot
Test Setup  Open Product Page    ${BASE_URL}  ${BROWSER}
Test Teardown  Close Browser


*** Variables ***
${BROWSER}  chrome
${BASE_URL}  localhost:80


*** Test Cases ***
Test Open Preview For Thumbnail
    [Documentation]    Tests opening a preview image for a thumbnail image of the product
    Open Thumbnail Image
    Check Preview Opened

Test Product Name In Alert
    [Documentation]    Tests that the product name is in the text of alert
    ${product_name}    Get Product Name
    Add Product To Cart
    Check ${product_name} In Alert

Test Product Name In Title
    [Documentation]    Tests that the product name is in the page title
    ${product_name}    Get Product Name
    Check ${product_name} In Title

