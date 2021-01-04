import pytest
from appium import webdriver
import unittest

import pathlib
from settings import *


@pytest.fixture()
def setup(request):
    # capabilities = {
    #     'platformName': (CONFIG[platform]['platformName']),
    #     'platformVersion': (CONFIG[platform]['platformVersion']),
    #     'deviceName': (CONFIG[platform]['deviceName']),
    #     'automationName': (CONFIG[platform]['automationName']),
    #     'appPackage': (CONFIG[platform]['appPackage']),
    #     'appActivity': (CONFIG[platform]['appActivity']),
    #     'noReset': (CONFIG[platform]['noReset']),
    #     'app': (CONFIG[platform]['folder'])
    # }

    app = os.path.abspath('../builds/app-d1g1t-dev-release.apk')
    print("Build: " + app)

    capabilities = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "app": app,
        "automationName": "uiautomator2",
        "appPackage": "d1g1twealth.d1g1t.com.d1g1t",
        "appWaitActivity": "d1g1twealth.d1g1t.com.ui.login.LoginActivity"
    }

    url = 'http://localhost:4723/wd/hub'
    request.instance.driver = webdriver.Remote(url, capabilities)
    request.instance.driver.implicitly_wait(30)


def teardown(request):
    request.instance.driver.quit()
    request.addfinalizer(teardown)
