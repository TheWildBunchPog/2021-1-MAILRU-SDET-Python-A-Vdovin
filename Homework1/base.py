import pytest
import basic_locators
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


CLICK_RETRY = 3


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def login(self):
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.element_to_be_clickable(basic_locators.ENTER)).click()
        login = self.find(basic_locators.LOGIN)
        login.clear()
        login.send_keys('kamabulletez@mail.ru')
        password = self.find(basic_locators.PASSWORD)
        password.clear()
        password.send_keys('bibletump123')
        self.find(basic_locators.LOG_IN).click()
        wait.until(EC.visibility_of_element_located(basic_locators.MAKE))

    def logout(self):
        wait = WebDriverWait(self.driver, timeout=10)
        self.find(basic_locators.MAIN).click()
        time.sleep(2)
        #wait.until(EC.visibility_of_element_located(basic_locators.LOG_OUT))
        self.find(basic_locators.LOG_OUT).click()
        wait.until(EC.visibility_of_element_located(basic_locators.ENTER))

    def edit_contacts(self, edit_name):
        wait = WebDriverWait(self.driver, timeout=10)
        self.find(basic_locators.PROFILE).click()
        wait.until(EC.visibility_of_element_located(basic_locators.FIO))
        fio = self.find(basic_locators.FIO)
        fio.clear()
        fio.send_keys(edit_name)
        self.find(basic_locators.SAVE).click()
        self.driver.refresh()
        wait.until(EC.visibility_of_element_located(basic_locators.FIO))

    def click_on_tabs(self, tabs, check_locator):
        wait = WebDriverWait(self.driver, timeout=10)
        self.find(tabs).click()
        wait.until(EC.visibility_of_element_located(check_locator))

    def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator)
                if i < 2:
                    self.driver.refresh()
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def verification(self, locator):
        try:
            self.find(locator)
        except NoSuchElementException:
            return False
        return True
