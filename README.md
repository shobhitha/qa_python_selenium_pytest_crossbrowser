# qa_python_selenium_pytest_crossbrowser

**Description**
This project performs testing of demo application Swag Labs (https://www.saucedemo.com) across different browsers (Chrome, Firefox, IE, Edge). Technologies used to automate the 
crossbrowser testing of Swag labs are: Python, Selenium, Pytest, Pytest-html (to generate reports), Pytest-xdist (for running tests in parallel). 

**Page Object Model Structure:**
    pageObjects - project pages/locators directory
    Reports - HTML reports directory
    testCases - project tests directory
    Configurations - config directory


**To install the packages this project requres:**
pip install -r requirements.txt 

**To run tests in terminal :**

pytest -v -s testCases/<test_file>.py

runs tests in parallel(-n option), creates html reports, --browser option let us mention the type of browser the test whould be run on 
pytest -v -s -n=2 --html=Reports/reports.html testCases/<test_file.py> --browser= <browser_name> (chrome, firefox, ie, edge)
