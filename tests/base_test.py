import pytest
from actions.login_actions import LoginActions


@pytest.mark.usefixtures('setup')
class BaseTests:

    login_email = "andriy.lizogubenko@d1g1t.com"
    login_password = "p@ssw0rd!"

    @pytest.fixture
    def init(self):
        driver = self.driver
        self.login_actions = LoginActions(driver)
