# Aloware-test-project
Test Project For Aloware

Tools used: 
### Pytest
### Selenium

# Project Structure

### config
configuration files
### helpers
helper files
### page
Pages - Page-Object model
### test_data
directory test data
### tests
directory for test files 

## Running instructions
* Download Project
* [Add chromedriver to path variable](https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver)
* Check installed packages:

`pip list`

`selenium         4.15.2`

`pytest           7.4.3`

if packaged are not present run

`pip install selenium pytest
`
* for running test cases run command

`pytest tests/test_demo.py --capture=no`