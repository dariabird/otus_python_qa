*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${THUMBNAIL_IMAGES}  css=a.thumbnail>img
${PREVIEW_IMAGE}    css=figure>img
${ITEM_NAME}    css=#content h1
${ADD_TO_CART_BUTTON}   css=#button-cart
${ALERT}    css=.alert-success


*** Keywords ***
Open Product Page
    [Arguments]     ${BASE_URL}  ${BROWSER}  ${PATH_ID}=57  ${PRODUCT_ID}=49
    Open Browser  url=http://${BASE_URL}/index.php?route=product/product&path=${PATH_ID}&product_id=${PRODUCT_ID}  browser=${BROWSER}   options=add_argument("--ignore-certificate-errors");add_argument("--start-maximized")

Open Thumbnail Image
    [Arguments]     ${NUM}=0
    Wait Until Element Is Visible    ${THUMBNAIL_IMAGES}
    ${thumbnails}    Get WebElements    ${THUMBNAIL_IMAGES}
    Click Element    ${thumbnails}[${NUM}]

Check Preview Opened
    Wait Until Element Is Visible   ${PREVIEW_IMAGE}

Get Product Name
    ${item_text}    Get Text    ${ITEM_NAME}
    [Return]    ${item_text}

Get Alert Text
    ${alert_text}   Get Text    ${ALERT}
    [Return]    ${alert_text}

Add Product To Cart
    Wait Until Element Is Visible    ${ADD_TO_CART_BUTTON}
    Click Element    ${ADD_TO_CART_BUTTON}

Check ${CUSTOM_TEXT} In Alert
    Wait Until Element Is Visible    ${ALERT}
    Element Should Contain    ${ALERT}    ${CUSTOM_TEXT}


Check ${CUSTOM_TEXT} In Title
    ${title}    Get Title
    Should Contain  ${CUSTOM_TEXT}   ${title}

