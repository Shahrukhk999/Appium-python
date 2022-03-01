from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
import click
import unittest
import pytest

class unitTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        desired_caps = {
            "platformName": "android",
            "version": "7.0",
            "deviceName": "infinix",
            "appPackage": "app.an10.ito.dev",
            "noReset": "True",
            "automationName": "appium",
            "app": "/home/shahrukh/Downloads/ITODev.apk",
            "udid": "02714107A0590149",
            "appActivity": "app.an10.ito.view.activities.SplashActivity"
        }
        self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
        self.Dropdown_button = "Open navigation drawer"
        self.click_on_EAM = "app.an10.ito.dev:id/tvScannedAsset"

    @pytest.mark.order1
    def test_scanned_asset(self):
        wait1 = WebDriverWait(self.driver, 20)
        self.driver.find_element_by_accessibility_id(self.Dropdown_button).click()
        self.driver.find_element_by_id(self.click_on_EAM).click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvScannedAsset").click()

        state = self.driver.find_element_by_id("app.an10.ito.dev:id/textViewSyncState")
        state.text
        if state.text == "Not Synced":
            self.driver.find_element_by_id("app.an10.ito.dev:id/btnSync").click()
            time.sleep(5)
        self.driver.find_element_by_accessibility_id("Navigate up").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvScannedAsset").click()
        state=wait1.until(EC.text_to_be_present_in_element((MobileBy.ID,"app.an10.ito.dev:id/textViewSyncState"),"Created"))

    @classmethod
    def tearDownClass(cls):
        print("testend")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

