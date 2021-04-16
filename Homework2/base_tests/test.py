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
        self.login_page.login(user_invalid, self.base_page.password)
        with allure.step('Find authorization error on page'):
            assert self.login_page.is_element_presented(self.login_page.locators.INVALID_LOGIN_OR_PASSWORD)

    @pytest.mark.UI
    def test_auth_invalid_password(self):
        password_invalid = 'error777'
        self.logger.info('Email - True, Password - False')
        self.login_page.login(self.base_page.user, password_invalid)
        with allure.step('Find authorization error on page'):
            assert self.login_page.is_element_presented(self.login_page.locators.INVALID_LOGIN_OR_PASSWORD)

    @pytest.mark.UI
    def test_create_campaign(self, auto):
        self.login_page = auto
        name_campaign = 'Test_campaign'
        self.main_page.go_to_campaigns().create_campaign(name_campaign, self.base_page.path_to_file)
        CHECKED_CAMPAIGN = (By.XPATH, f'//a[contains(@title,"{name_campaign}" )]/../label/input[@checked]')
        with allure.step('Find campaign on page'):
            assert self.base_page.is_element_presented(CHECKED_CAMPAIGN)
        self.campaign_page.delete_campaign(name_campaign)

    @pytest.mark.UI
    def test_create_segment(self, auto):
        self.login_page = auto
        name_segment = 'Test segment'
        self.main_page.go_to_audience().create_segment(name_segment)
        CHECKED_SEGMENT = (By.XPATH, f'//a[@title="{name_segment}"]')
        with allure.step('Find segment on page'):
            assert self.base_page.is_element_presented(CHECKED_SEGMENT)
        self.audience_page.delete_segment(name_segment)

    @pytest.mark.UI
    def test_delete_segment(self, auto):
        self.login_page = auto
        name_segment = 'Test delete segment'
        self.main_page.go_to_audience().create_segment(name_segment)
        self.audience_page.delete_segment(name_segment)
        CHECKED_SEGMENT = (By.XPATH, f'//a[@title="{name_segment}"]')
        self.driver.refresh()
        with pytest.raises(TimeoutException):
            self.base_page.find(CHECKED_SEGMENT, timeout=10)
