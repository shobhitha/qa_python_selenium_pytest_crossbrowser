# qa_python_selenium_pytest_crossbrowser

Automated crossbrowser testing of Swag Labs (https://www.saucedemo.com) application using Python, Selenium, Pytest, Pytest-html, Pytest-xdist (for running tests in parallel). The tests run on chrome, firefox, IE, Edge.

pip install -r requirements.txt will install all the packages this project require

Usage:
pytest -v -s -n=2 --html=Reports/reports.html testCases/test_login.py —browser chrome, firefox, ie, edge
