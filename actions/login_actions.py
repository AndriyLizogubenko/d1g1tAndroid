from actions.base_action import BaseAction
from pages.login_screen import LoginScreen
import time

class LoginActions(BaseAction):

    def __init__(self, driver):
        self.driver = driver

    def login_steps(self, email, password):
        self.driver.find_element_by_id("d1g1twealth.d1g1t.com.d1g1t:id/email").send_keys(email)
        self.driver.find_element_by_id("d1g1twealth.d1g1t.com.d1g1t:id/password").send_keys(password)
        self.driver.find_element_by_id(LoginScreen.login_btn_id).click()

    def logout_steps(self):
        self.driver.find_element_by_id("d1g1twealth.d1g1t.com.d1g1t:id/settings_button").click()
        #for small screens - if Sign Out is not visible swipe up
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Sign out']").click()
        self.driver.find_element_by_id("android:id/button1").click()

    def forgor_password_steps(self, email):
        self.driver.find_element_by_id("d1g1twealth.d1g1t.com.d1g1t:id/forgot_password_text").click()
        self.driver.find_element_by_id("d1g1twealth.d1g1t.com.d1g1t:id/user_email").send_keys(email)
        self.driver.find_element_by_id("d1g1twealth.d1g1t.com.d1g1t:id/forgot_password_text").click()
