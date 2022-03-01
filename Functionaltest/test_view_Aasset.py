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
        self.click_on_view_asset="app.an10.ito.dev:id/tvViewAsset"
        self.scan_qrcode="app.an10.ito.dev:id/ivQrCodeSuccess"
        self.partno="app.an10.ito.dev:id/tvFacilityModelPartNo"



    @pytest.mark.order1
    def test_classifed_asset(self):
        wait1 = WebDriverWait(self.driver, 20)
        self.driver.find_element_by_accessibility_id(self.Dropdown_button).click()
        self.driver.find_element_by_id(self.click_on_EAM).click()
        self.driver.find_element_by_id(self.click_on_view_asset).click()
        self.driver.find_element_by_id(self.scan_qrcode).click()
        asset_id= wait1.until(EC.text_to_be_present_in_element((MobileBy.ID, self.partno), "RD-NB-RK-0001-000004"))
        self.driver.find_element_by_id("app.an10.ito.dev:id/ivAssetInformationImages").is_displayed()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvVAIFacilityName").is_displayed()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvVAIBLTAGValue").is_displayed()
        TouchAction(self.driver).press(x=720, y=1243).move_to(x=708, y=1181).release().perform()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvVAICategoryNameValue").is_displayed()

    @pytest.mark.order2
    def test_nonexisting_scanned_asset(self):
        wait1 = WebDriverWait(self.driver, 20)
        self.driver.find_element_by_accessibility_id(self.Dropdown_button).click()
        self.driver.find_element_by_id(self.click_on_EAM).click()
        self.driver.find_element_by_id(self.click_on_view_asset).click()
        self.driver.find_element_by_id(self.scan_qrcode).click()
        print(self.driver.find_element_by_id("app.an10.ito.dev:id/snackbar_text").text)

    @pytest.mark.order3
    def test_unclassidiedasset(self):
        wait1 = WebDriverWait(self.driver, 20)
        self.driver.find_element_by_accessibility_id(self.Dropdown_button).click()
        self.driver.find_element_by_id(self.click_on_EAM).click()
        self.driver.find_element_by_id(self.click_on_view_asset).click()
        self.driver.find_element_by_id(self.scan_qrcode).click()
        part_no = self.driver.find_element_by_id("app.an10.ito.dev:id/tvFacilityModelPartNo")
        if part_no.is_displayed():
            print("testfail")
        else:
            print("testpass")

    @classmethod
    def tearDownClass(cls):
        print("testend")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

