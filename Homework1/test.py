import pytest
from base import BaseCase
import basic_locators


class TestOne(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login()
        assert "Создайте рекламную кампанию" in self.driver.page_source

    @pytest.mark.UI
    def test_logout(self):
        self.login()
        self.logout()
        assert "Войти" in self.driver.page_source

    @pytest.mark.UI
    def test_edit_contacts(self):
        self.login()
        self.edit_contacts()
        assert "Иван Иванов" in self.driver.page_source

    @pytest.mark.parametrize(
        'tabs',
        [
            pytest.param(
                basic_locators.BALANCE
            ),
            pytest.param(
                basic_locators.STATISTIC
            ),
        ]
    )

    @pytest.mark.UI
    def test_click_on_tabs(self, tabs):
        self.login()
        self.click_on_tabs(tabs)
        if tabs == basic_locators.BALANCE:
            assert "Автопополнение" in self.driver.page_source
        elif tabs == basic_locators.STATISTIC:
            assert "Конструктор отчётов" in self.driver.page_source
