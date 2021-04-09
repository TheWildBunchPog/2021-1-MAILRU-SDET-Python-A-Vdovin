import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.campaign_page import CampaignPage
from ui.pages.audience_page import AudiencePage


WAIT_TIME = 20


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.campaign_page: CampaignPage = request.getfixturevalue('campaign_page')
        self.audience_page: AudiencePage = request.getfixturevalue('audience_page')

        self.logger.debug('Initial setup done!')
