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

    @pytest.mark.order1
    def test_facility_profile(self):
        self.driver.find_element_by_accessibility_id("Open navigation drawer").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvScannedAsset").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvEAMDatabase").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/search_src_text").send_keys("Warehouse")
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvEAMFacilitiesListAssetName").click()
        time.sleep(1)
        #self.driver.find_element_by_accessibility_id("Warehouse.").click()
        self.driver.find_element_by_xpath("//android.support.v7.app.ActionBar.Tab[@content-desc='Facility']/android.widget.TextView").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/textView24").click()
        nessame=self.driver.find_element_by_id("app.an10.ito.dev:id/tvNoFacilityImagesFound")
        print(nessame.text)
        self.driver.find_element_by_id("app.an10.ito.dev:id/imageView10").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/textView23").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvFacilityFieldsNameValue").is_displayed()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvAddressValue").is_displayed()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvRegionNameValue").is_displayed()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvCountryValue").is_displayed()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvOwnerShipStatusValue").is_displayed()
        self.driver.find_element_by_id("app.an10.ito.dev:id/imageView9").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/textView25").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvFacilityFieldsNameValue").is_displayed()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvFacilityFieldsName").is_displayed()
        self.driver.find_element_by_id("app.an10.ito.dev:id/searchView").send_keys("2G vendor")
        self.driver.hide_keyboard()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvFacilityFieldsName").is_displayed()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvFacilityFieldsNameValue").is_displayed()
        #self.driver.tap(([(995, 1809)]))
        self.driver.find_element_by_xpath("//android.support.v7.app.ActionBar.Tab[@content-desc='Inventory']/android.widget.TextView").click()
        self.driver.find_element_by_id("app.an10.ito.dev:id/tvSelectedFacilityAssetName").is_displayed()

        #time.sleep(10)


    @classmethod
    def tearDownClass(cls):
            print("testend")
            cls.driver.quit()

if __name__ == '__main__':
        unittest.main()

