import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from ui.locators.basic_locators import BasePageLocators
import os


WAIT_TIME = 5
CLICK_RETRY = 3
BASE_TIMEOUT = 10


class BasePage(object):

    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver
        self.user = 'kamabulletez@mail.ru'
        self.password = 'bibletump123'
        self.path_to_file = os.path.dirname(os.path.abspath(__file__)) + '/data/kekwait.jpg'

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step('Click')
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def is_element_presented(self, locator):
        try:
            self.find(locator)
        except NoSuchElementException:
            return False
        return True
