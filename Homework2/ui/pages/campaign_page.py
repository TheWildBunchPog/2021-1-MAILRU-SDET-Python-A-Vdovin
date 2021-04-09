import allure

from ui.pages.main_page import MainPage
from ui.locators.basic_locators import CampaignPageLocators
from selenium.webdriver.common.by import By


class CampaignPage(MainPage):
    locators = CampaignPageLocators()

    def create_campaign(self, name, file):
        try:
            self.find(self.locators.CREATE_CAMPAIGN, timeout=15).is_displayed()
            self.find(self.locators.CREATE_CAMPAIGN).click()
        except:
            self.find(self.locators.CREATE_FIRST_CAMPAIGN, timeout=15).click()
        self.click(self.locators.TRAFFIC)
        self.find(self.locators.ENTER_LINK).send_keys('https://github.com/TheWildBunch1')
        self.click(self.locators.CLEAR_NAME_CAMPAIGN)
        with allure.step('Find and send name campaign'):
            self.find(self.locators.NAME_CAMPAIGN).send_keys(name)
        self.click(self.locators.BANNER)
        with allure.step('Upload image campaign'):
            self.find(self.locators.UPLOAD_IMAGE).send_keys(file)
        self.click(self.locators.SAVE_AD)
        self.click(self.locators.CONFIRM_CREATE_CAMPAIGN)

    def delete_campaign(self, name_campaign):
        CHOOSE_CAMPAIGN = (By.XPATH, f"//a[@title='" + name_campaign + "']/../input[@type='checkbox']")
        with allure.step('Search created company'):
            self.click(CHOOSE_CAMPAIGN)
        self.click(self.locators.ACTION_MENU)
        self.click(self.locators.DELETE_CAMPAIGN)
