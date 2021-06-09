import allure
from allure_commons.types import AttachmentType
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
RETRY_COUNT = 20


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=20) -> WebElement:
        return WebDriverWait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def click(self, locator, timeout=20):
        # попытки чтобы кликнуть
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = WebDriverWait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def screenshot(self, name):
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)

    def is_element_presented(self, locator):
        try:
            self.find(locator)
        except NoSuchElementException:
            return False
        return True

    def is_vk_id_presented(self, locator):
        try:
            self.find(locator, timeout=1)
            return True
        except TimeoutException:
            return False
