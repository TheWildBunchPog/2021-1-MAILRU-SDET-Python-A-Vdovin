import allure
import pytest
from base import BaseCase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class TestOne(BaseCase):

    @pytest.mark.UI
    def test_auth_invalid_email(self):
        user_invalid = 'error123@mail.ru'
        self.logger.info('Email - False, Password - True')
        self.base_page.login(user_invalid, self.base_page.password)
        with allure.step('Find authorization error on page'):
            assert self.base_page.verification(self.base_page.locators.INVALID_LOGIN_OR_PASSWORD)

    @pytest.mark.UI
    def test_auth_invalid_password(self):
        password_invalid = 'error777'
        self.logger.info('Email - True, Password - False')
        self.base_page.login(self.base_page.user, password_invalid)
        with allure.step('Find authorization error on page'):
            assert self.base_page.verification(self.base_page.locators.INVALID_LOGIN_OR_PASSWORD)

    @pytest.mark.UI
    def test_create_campaign(self, auto):
        self.base_page = auto
        self.main_page.go_to_campaigns()
        name_campaign = 'Test_campaign'
        self.campaign_page.create_campaign(name_campaign, self.base_page.path_to_file)
        CHECKED_CAMPAIGN = (By.XPATH, '//a[contains(@title,"' + name_campaign + '" )]/../label/input[@checked]')
        with allure.step('Find campaign on page'):
            assert self.base_page.verification(CHECKED_CAMPAIGN)
        self.campaign_page.delete_campaign(name_campaign)

    @pytest.mark.UI
    def test_create_segment(self, auto):
        self.base_page = auto
        self.main_page.go_to_audience()
        name_segment = 'Test segment'
        self.audience_page.create_segment(name_segment)
        CHECKED_SEGMENT = (By.XPATH, '//a[@title="'+name_segment+'"]')
        with allure.step('Find segment on page'):
            assert self.base_page.verification(CHECKED_SEGMENT)
        self.audience_page.delete_segment(name_segment)

    @pytest.mark.UI
    def test_delete_segment(self, auto):
        self.base_page = auto
        self.main_page.go_to_audience()
        name_segment = 'Test delete segment'
        self.audience_page.create_segment(name_segment)
        self.audience_page.delete_segment(name_segment)
        CHECKED_SEGMENT = (By.XPATH, '//a[@title="' + name_segment + '"]')
        self.driver.refresh()
        with pytest.raises(TimeoutException):
            self.base_page.find(CHECKED_SEGMENT, timeout=10)
