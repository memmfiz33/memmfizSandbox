from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')

class LoginPageLocators:
    EMAIL_INPUT_LOGIN = (By.ID, 'id_login-username')
    PASSWORD_INPUT_LOGIN = (By.ID, 'id_login-password')



