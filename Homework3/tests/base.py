import pytest
from utils.builder import Builder


class ApiBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.builder = Builder()
