*** Settings ***

Documentation  Example that opens single page

Library  Browser
        ...  enable_playwright_debug=${True}
        ...  auto_closing_level=TEST
        ...  retry_assertions_for=0:00:03
Library  unstable_url.py


Force Tags  ui

*** Variables ***

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
  ${url} =  Get Unstable Url
  New Page   ${url}
  Get Title  ==  URN.SU
  Close Browser