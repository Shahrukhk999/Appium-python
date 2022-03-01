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
        # driver.implicitly_wait(5000)
        self.driver.implicitly_wait(5)

    @pytest.mark.order2
    def test_facility_profile(self):
        self.driver.find_element_by_accessibility_id("Open navigation drawer").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvScannedAsset").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvEAMDatabase").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/search_src_text").send_keys("Warehouse")
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvEAMFacilitiesListAssetName").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/et_search").send_keys("FeederCable")
        name=self.driver.find_element_by_id("app.an10.ito.dev:id/tvInventoryModel")
        self.assertEqual("FeederCable", name.text)

    @pytest.mark.order1
    def test_search_asset(self):
        self.driver.find_element_by_accessibility_id("Open navigation drawer").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvScannedAsset").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvEAMDatabase").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/search_src_text").send_keys("Warehouse")
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvEAMFacilitiesListAssetName").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/imageButton").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/spinnerClassCategories").click()
       # time.sleep(0.4)
        self.driver.tap(([(172, 475)]))
        self.driver.find_element_by_id("app.an10.ito.dev:id/spinnerClassSubCategories").click()
      #  time.sleep(0.5)
        self.driver.tap(([(179, 590)]))
        self.driver.find_element_by_id("app.an10.ito.dev:id/spinnerAssetClass").click()
       # time.sleep(0.1)
        self.driver.tap(([(284, 771)]))
        self.driver.find_element_by_id("app.an10.ito.dev:id/btnFilter").click()
        result= self.driver.find_element_by_id("app.an10.ito.dev:id/tvSelectedFacilityAssetName")
        result.text
        self.assertEqual("PW-GN-RH-0001-000004", result.text)


