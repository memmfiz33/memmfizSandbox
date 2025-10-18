import pytest
import os
import sys
from selenium import webdriver

project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                      help="Choose language: en, ru, fr")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if not user_language:
        raise Exception("Please choose language: e.g.'--language=es'")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {'intl.accept_languages' : user_language})
    browser = webdriver.Chrome(options=options)
    print(f"\nStart Chrome browser with language: {user_language}")

    yield browser
    print("\nquit browser..")
    browser.quit()

