import pytest
from time import sleep
from tests.base_test import BaseTests
from pages.login_screen import LoginScreen
from pages.main_screen import MainScreen


class TestHome(BaseTests):

    # open the app, login, background, foreground, verify home screen elements are displayed
    def test_background(self, init):
        self.login_actions.login_steps(email=self.login_email, password=self.login_password)
        sleep(5)
        assert self.driver.find_element_by_id("d1g1twealth.d1g1t.com.d1g1t:id/settings_button").is_displayed()
        self.driver.background_app(3)
        assert self.driver.find_element_by_id("d1g1twealth.d1g1t.com.d1g1t:id/settings_button").is_displayed()