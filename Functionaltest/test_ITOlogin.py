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
    '''
           in this function we are initalizing our pre requirements like selectors, appium server address and desired capabilities
           descired caps are basically information for appium to configure device.
           '''

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
        self.signin_button="app.an10.ito.dev:id/btnSignIn"
        self.username="app.an10.ito.dev:id/tvEmail"
        self.passowrd="app.an10.ito.dev:id/tvPassword"
        self.login="app.an10.ito.dev:id/btnLogin"
        self.error_message="app.an10.ito.dev:id/snackbar_text"
    '''there are six different test to check login for ITO in these tests we we automate all the ,anual steps we have to do to test login screen manually'''

    @pytest.mark.order1
    def test_login_with_wrongusername_correct_password(self):
        signin = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.signin_button)))
        signin.click()
        # time.sleep(10)
        username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.username)))
        username.send_keys("aavuz")
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.passowrd)))
        password.send_keys("test12")
        self.driver.hide_keyboard()

        login = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.login)))
        login.click()
        error = self.driver.find_element_by_id(self.error_message)
        self.assertEqual("Minimum name length 6", error.text)

        print(error.text)

    @pytest.mark.order2
    def test_login_with_correctusername_wrong_password(self):
        signin = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.signin_button)))
        signin.click()
        # time.sleep(10)
        username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.username)))
        username.send_keys("maavuz")
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.passowrd)))
        password.send_keys("test12")
        self.driver.hide_keyboard()


        login = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.login)))
        login.click()
        error = self.driver.find_element_by_id(self.error_message)
        self.assertEqual("Invalid user credentials", error.text)

        print(error.text)

    @pytest.mark.order3
    def test_passowrd_length(self):
        signin = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.signin_button)))
        signin.click()
        # time.sleep(10)
        username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.username)))
        username.send_keys("maavuz")
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.passowrd)))
        password.send_keys("test")
        self.driver.hide_keyboard()

        login = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.login)))
        login.click()
        error = self.driver.find_element_by_id(self.error_message)
        self.assertEqual("Minimum password length", error.text)

    @pytest.mark.order4
    def test_login_with_nousername(self):
        signin = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.signin_button)))
        signin.click()
        # time.sleep(10)
        username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.username)))
        username.send_keys("")
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.passowrd)))
        password.send_keys("test12")
        self.driver.hide_keyboard()

        login = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.login)))
        login.click()
        error = self.driver.find_element_by_id(self.error_message)
        self.assertEqual("Email is required", error.text)

    @pytest.mark.order6
    def test_correct_username_password(self):
        signin = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.signin_button)))
        signin.click()
        # time.sleep(10)
        username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.username)))
        username.send_keys("maavuz")
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.passowrd)))
        password.send_keys("test123")
        self.driver.hide_keyboard()

        login = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.login)))
        login.click()

        homepage=self.driver.find_element_by_accessibility_id("Open navigation drawer")
        homepage.is_displayed()

    @pytest.mark.order5
    def test_both_empty(self):
        signin = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.signin_button)))
        signin.click()
        # time.sleep(10)
        username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((MobileBy.ID, self.username)))
        username.send_keys("")
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.passowrd)))
        password.send_keys("")
        self.driver.hide_keyboard()

        login = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((MobileBy.ID, self.login)))
        login.click()
        error = self.driver.find_element_by_id(self.error_message)
        self.assertEqual("Email is required", error.text)
    @classmethod
    def tearDownClass(cls):
        print("testend")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

