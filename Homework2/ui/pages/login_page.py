from ui.locators.basic_locators import LoginPageLocators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def login(self, user, password):
        self.find(LoginPageLocators.ENTER).click()
        login = self.find(LoginPageLocators.LOGIN)
        login.clear()
        login.send_keys(user)
        password_field = self.find(LoginPageLocators.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)
        self.find(LoginPageLocators.LOG_IN).click()
