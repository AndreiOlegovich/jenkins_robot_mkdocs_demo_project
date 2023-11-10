*** Settings ***
Documentation  Example that opens single page

Library  Browser
        ...  enable_playwright_debug=${True}
        ...  auto_closing_level=TEST
        ...  retry_assertions_for=0:00:03
Library  Collections
Library  DateTime

Force Tags  ui

*** Variables ***

${url}  https://eth1.ru


*** Keywords ***

Test Setup Tasks
  Start Chromium Browser

Test Teardown Tasks
  Close Browser

Start Chromium Browser
  New Browser  browser=chromium  headless=True
  New Context  viewport={'width': 1920, 'height': 1080}  ignoreHTTPSErrors=True

*** Test Cases ***

Starting a browser with a page
  [Tags]    title
  New Page    https://www.urn.su/qa/ui/basic_test/
  Get Title  ==  UI Test Page
  Close Browser


Fill Field
  [Tags]    field
  New Page    https://www.urn.su/qa/ui/basic_test/
  Fill Text  //input[@id="name1"]    topbicycle.ru
  Click    //input[@id="submit1"]
  Get Title    ==    TopBicycle.ru
  Close Browser


Renovation
  [Tags]    renovation
  New Page    https://www.urn.su/qa/ui/basic_test/
  ${urls}=    Get Elements  text="Renovation"
  # depends on Collections lib
  ${url0}=    Get From List    ${urls}    0
  Click    ${url0}
  Get Title    ==    Ремонт квартир на Коста-дель-Соль
  Close Browser


Italy
  [Tags]    italy
  New Page    https://www.urn.su/qa/ui/basic_test/
  ${urls}=    Get Elements    //a[@class="march8"]
  # depends on Collections lib
  Log    ${urls}
  ${url0}=    Get From List    ${urls}    0
  Click    ${url0}
  # datetime formate allowes attributes
  ${date}=  Get Current Date  result_format=datetime
  Get Title    ==    8 марта в Италии в ${date.year} году
  Close Browser


Img
  [Tags]    img
  New Page    https://www.urn.su/qa/ui/basic_test/
  ${images}=    Get Elements    //img[@class="w100 firstimage"]
  # depends on Collections lib
  ${img0}=    Get From List    ${images}    1
  Click    ${img0}
  Get Title    ==    Тренировка для людей с проблемами со спиной и позвоночником
  Close Browser


Radio Buttons
  [Tags]    radio
  New Page    https://www.urn.su/qa/ui/basic_test/
  ${buttons}=    Get Elements    //input[@name="house"]
  # depends on Collections lib
  ${button0}=    Get From List    ${buttons}    0
  ${button2}=    Get From List    ${buttons}    2
  Get Element States    ${button0}    validate    checked
  Check Checkbox    ${button2}
  Get Element States    ${button0}    not contains    checked
  Get Element States    ${button2}    validate    checked


Checkboxes
  [Tags]    checkbox
  New Page    https://www.urn.su/qa/ui/basic_test/
  ${cersei}=    Get Element    //input[@id="cerseiId"]
  Check Checkbox    ${cersei}
  Get Element States    ${cersei}    validate    checked


Dropdown
  [Tags]    dropdown
  New Page    https://www.urn.su/qa/ui/basic_test/
  Select Options By    css=#swords    value    dawn
  Get Element States    //option[@value="dawn"]    contains    selected


Table
  [Tags]    table
  New Page    https://www.urn.su/qa/ui/basic_test/
  ${table}=    Get Element    //table[@class="basictable"]
  ${tb_topic}=    Get Table Cell Element    ${table}    "Topic"    "2018"
  Get Text    ${tb_topic}    ==    Bicycles
  ${hh_topic}=    Get Table Cell Element    ${table}    1    1
  Get Text    ${hh_topic}    ==    Travel, Holidays


Nested Table
  [Tags]    nested_table
  New Page    https://www.urn.su/qa/ui/basic_test/

  ${table}=    Get Element    //table[@class="houses tcont5"]
  ${st}=    Get Table Cell Element    ${table}    0    0
  Get Text    ${st}    ==    Starks

  ${nested}=    Get Element    xpath=//html/body/main/table[3]/tbody/tr/td[2]/table
  ${r}=    Get Table Cell Element    ${nested}    0    2
  Get Text    ${r}    ==    Rob


Upload File
  [Tags]    upload
  New Page    https://www.devhops.ru/login/free_upload/
  Upload File By Selector    //input[@type="file"]    heihei_logo.jpg
  Click    id=submit
  Get Title    ==    Success





