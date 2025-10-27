from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')

class LoginPageLocators:
    # login form
    URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    EMAIL_INPUT_LOGIN = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD_INPUT_LOGIN = (By.CSS_SELECTOR, '#id_login-password')

    # registration form
    EMAIL_INPUT_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_INPUT_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_CONFIRMATION_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-password2')

class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME  = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_ALERT = (By.CSS_SELECTOR, ".alert-info strong")


    ## SECOND_SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert-success:has(strong:contains(\"The shellcoder's handbook\"))")





