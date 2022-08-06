import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Set language: [en-gb, ru, es]")

                    
def pytest_generate_tests(metafunc):
    option_value = metafunc.config.getoption("language")
    if 'language' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("language", [option_value])

@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


