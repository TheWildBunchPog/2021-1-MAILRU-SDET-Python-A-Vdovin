from ui.locators.locators import RegistrationPageLocators
from ui.pages.base_page import BasePage


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()

    def registration(self, username, email, password, confirm_password, accept=True):
        self.find(self.locators.GO_TO_CREATE_ACCOUNT).click()
        self.find(self.locators.USERNAME_FIELD).send_keys(username)
        self.find(self.locators.EMAIL_FIELD).send_keys(email)
        self.find(self.locators.PASSWORD_FIELD).send_keys(password)
        self.find(self.locators.CONFIRM_PASSWORD_FIELD).send_keys(confirm_password)
        if accept is True:
            self.find(self.locators.ACCEPT).click()
        self.find(self.locators.REGISTER_SUBMIT).click()
