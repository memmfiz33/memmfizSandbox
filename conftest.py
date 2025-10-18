import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
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