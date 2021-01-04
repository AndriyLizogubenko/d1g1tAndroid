import pytest
from time import sleep
from tests.base_test import BaseTests
from pages.login_screen import LoginScreen
from pages.main_screen import MainScreen

class TestLogin(BaseTests):


    def test_login(self, init):
        self.login_actions.login_steps(email= self.login_email, password= self.login_password)
        self.driver.find_element_by_id("d1g1twealth.d1g1t.com.d1g1t:id/settings_button").is_displayed()


    def test_logout(self, init):
        self.login_actions.login_steps(email= self.login_email, password= self.login_password)
        sleep(5)
        self.login_actions.logout_steps()
        self.driver.find_element_by_id(LoginScreen.login_btn_id).is_displayed()


    #test cases for background and foreground app it should be implemented for most of the screens
    #open the app, backgound, foreground, verify login elements are shown
    def test_background(self, init):
        self.driver.background_app(2)
        assert self.driver.find_element_by_id(LoginScreen.login_btn_id).is_displayed()


    def test_incorrect_email(self, init):
        self.login_actions.login_steps(email="incorrect@d1g1t.com", password="correct")
        sleep(5)
        assert self.driver.find_element_by_id(LoginScreen.login_btn_id).is_displayed()

        #driver.find_elements_by_xpath('//[contains(text(), "' + Incorrect credentials, try again + '")]')
        #(//android.widget.ImageButton[@content-desc="Error"])[2]

        # - when the user on login screen
        # - when the user on home screen


        # def test_forgot_password(self, init):
        #   self.login_actions.forgor_password_steps(email="andriy.lizogubenko@d1g1t.com")
        #   assert self.driver.find_element_by_id(LoginScreen.login_btn_id)