import allure

from ui.pages.base_page import BasePage
from ui.pages.campaign_page import CampaignPage
from ui.pages.audience_page import AudiencePage
from ui.locators.basic_locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()

    def go_to_campaigns(self):
        with allure.step('Click on campaign tab'):
            self.click(self.locators.CAMPAIGNS)
        return CampaignPage(self.driver)

    def go_to_audience(self):
        with allure.step('Click on audience tab'):
            self.click(self.locators.AUDIENCE)
        return AudiencePage(self.driver)
