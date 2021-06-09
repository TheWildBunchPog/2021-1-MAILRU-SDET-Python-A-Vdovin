from selenium.webdriver import ActionChains

from ui.locators.locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def go_to_python(self):
        self.find(self.locators.PYTHON).click()

    def go_to_python_history(self):
        ActionChains(self.driver).move_to_element(self.find(self.locators.PYTHON)).perform()
        self.find(self.locators.PYTHON_HISTORY).click()

    def go_to_about_flask(self):
        ActionChains(self.driver).move_to_element(self.find(self.locators.PYTHON)).perform()
        self.find(self.locators.ABOUT_FLASK).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def go_to_download_centos7(self):
        ActionChains(self.driver).move_to_element(self.find(self.locators.LINUX)).perform()
        self.find(self.locators.DOWNLOAD_CENTOS).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def go_to_network_wireshark_news(self):
        ActionChains(self.driver).move_to_element(self.find(self.locators.NETWORK)).perform()
        self.find(self.locators.WIRESHARK_NEWS).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def go_to_network_wireshark_download(self):
        ActionChains(self.driver).move_to_element(self.find(self.locators.NETWORK)).perform()
        self.find(self.locators.WIRESHARK_DOWNLOAD).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def go_to_network_tcpdump_examples(self):
        ActionChains(self.driver).move_to_element(self.find(self.locators.NETWORK)).perform()
        self.find(self.locators.TCPDUMP_EXAMPLES).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def go_to_api_wikipedia(self):
        self.find(self.locators.API_WIKIPEDIA).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def go_to_future_of_internet(self):
        self.find(self.locators.FUTURE_OF_INTERNET).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def go_to_smtp_wikipedia(self):
        self.find(self.locators.SMTP_WIKIPEDIA).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
