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
    def test_check_home_title(self):
        title=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        self.assertEqual("ITO HOME", title.text)

    @pytest.mark.order2
    def test_check_map(self):
        map= self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]")
        map.is_displayed()

    @pytest.mark.order3
    def test_dropdown_button(self):
        self.driver.find_element_by_accessibility_id("Open navigation drawer").click()

    @pytest.mark.order4
    def test_map_button(self):
        map_button=self.driver.find_element_by_accessibility_id("My Location")
        map_button.is_displayed()


    @classmethod
    def tearDownClass(cls):
        print("testend")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

