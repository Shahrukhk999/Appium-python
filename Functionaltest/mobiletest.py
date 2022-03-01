from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
import unittest
import click
class unitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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
        driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
        # driver.implicitly_wait(5000)
        driver.implicitly_wait(5)

    def test_login(self):

#driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup").click()
        inputA = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((MobileBy.ID, "app.an10.ito.dev:id/btnSignIn")))
        inputA.click()
#time.sleep(10)
        inputB = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((MobileBy.ID, "app.an10.ito.dev:id/tvEmail")))
        inputB.send_keys("aavuz")
        inputc = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((MobileBy.ID, "app.an10.ito.dev:id/tvPassword")))
        inputc.send_keys("test123")
        self.driver.hide_keyboard()
#inputB.clear()


        inputd = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((MobileBy.ID, "app.an10.ito.dev:id/btnLogin")))
        inputd.click()
        error= self.driver.find_element_by_id("app.an10.ito.dev:id/snackbar_text")
        self.assertEqual("sadad", error.text)

        print(error.text)


time.sleep(10)
#driver.find_element_by_accessibility_id("Open navigation drawer").click()
#driver.find_element_by_id("app.an10.ito.dev:id/tvScannedAsset").click()
#time.sleep(10)
#driver.find_element_by_id("app.an10.ito.dev:id/clViewAsset").click()
#time.sleep(10)
#driver.find_element_by_id("app.an10.ito.dev:id/ivQrCodeSuccess").click()
#time.sleep(5)
#name = driver.find_element_by_id("app.an10.ito.dev:id/tvVAIFacilityName").text
#if name == "tst1010":
#    print("test pass")
#else:
#    print("test fail")



#driver.quit()