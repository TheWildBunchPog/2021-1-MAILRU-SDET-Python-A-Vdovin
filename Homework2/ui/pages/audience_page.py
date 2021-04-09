import allure
from selenium.common.exceptions import TimeoutException
from ui.pages.main_page import MainPage
from ui.locators.basic_locators import AudiencePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AudiencePage(MainPage):
    locators = AudiencePageLocators()

    def create_segment(self, name_segment):
        try:
            self.wait(timeout=15).until(EC.element_to_be_clickable(self.locators.CREATE_FIRST_SEGMENT)).click()
        except TimeoutException:
            self.wait(timeout=15).until(EC.element_to_be_clickable(self.locators.CREATE_SEGMENT)).click()
            self.click(self.locators.APPS_AND_GAMES)
        self.click(self.locators.CHECK_BOX_PROPERTY)
        self.click(self.locators.ADD_SEGMENT)
        with allure.step('Find and send name segment'):
            input_name = self.find(self.locators.INPUT_NAME_SEGMENT)
            input_name.clear()
            input_name.send_keys(name_segment)
        self.click(self.locators.CREATE_SEGMENT)
        with allure.step('Search created segment'):
            self.find(self.locators.CREATE_SEGMENT, timeout=10).is_displayed()

    def delete_segment(self, name_segment):
        self.go_to_audience()
        with allure.step('Search created segment'):
            self.find(self.locators.INPUT_SEARCH_SEGMENT).send_keys(name_segment)
        SEGMENT_SEARCH = (By.XPATH, '//li[@title="'+name_segment+'"]')
        self.click(SEGMENT_SEARCH)
        self.click(self.locators.DELETE_SEGMENTS)
        self.click(self.locators.SUBMIT_DELETE)
