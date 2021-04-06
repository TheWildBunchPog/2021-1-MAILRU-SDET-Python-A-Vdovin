import pytest
from base import BaseCase
import basic_locators


class TestOne(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login()
        assert self.verification(basic_locators.MAIN)

    @pytest.mark.UI
    def test_logout(self):
        self.login()
        self.logout()
        assert self.verification(basic_locators.ENTER)

    @pytest.mark.UI
    def test_edit_contacts(self):
        self.login()
        edit_name = 'ANTON IVANOV'
        self.edit_contacts(edit_name)
        assert self.find(basic_locators.FIO).get_attribute('value') == edit_name

    @pytest.mark.parametrize(
        'tabs, check_locator',
        [
            pytest.param(
                basic_locators.BALANCE, basic_locators.SCORE
            ),
            pytest.param(
                basic_locators.STATISTIC, basic_locators.SUMMARY
            ),
        ]
    )
    @pytest.mark.UI
    def test_click_on_tabs(self, tabs, check_locator):
        self.login()
        self.click_on_tabs(tabs, check_locator)
        assert self.verification(check_locator)
