from ui.locators.locators import LoginPageLocators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def login(self, username, password):
        self.find(self.locators.USERNAME_FIELD).send_keys(username)
        self.find(self.locators.PASSWORD_FIELD).send_keys(password)
        self.find(self.locators.LOGIN_SUBMIT).click()

    def go_to_create_account(self):
        self.click(self.locators.GO_TO_CREATE_ACCOUNT)

    def logout(self, username, password):
        self.find(self.locators.USERNAME_FIELD).send_keys(username)
        self.find(self.locators.PASSWORD_FIELD).send_keys(password)
        self.find(self.locators.LOGIN_SUBMIT).click()
        self.find(self.locators.LOGOUT).click()
