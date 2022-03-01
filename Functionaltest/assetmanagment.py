from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time
import click

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
#driver.implicitly_wait(5000)
driver.implicitly_wait(5)
driver.hide_keyboard()
'''

'''
driver.find_element_by_accessibility_id("Open navigation drawer").click()
driver.find_element_by_id("app.an10.ito.dev:id/tvScannedAsset").click()
driver.find_element_by_id("app.an10.ito.dev:id/tvAssetManagement").click()
time.sleep(5)
driver.find_element_by_accessibility_id("tst1010. 5bf64eaff290463aedd03fb2.").click()

time.sleep(5)
driver.tap([(533, 873)])
#TouchAction().press(533, 873).release()
driver.find_element_by_id("app.an10.ito.dev:id/btnAddNewAsset").click()
time.sleep(5)
name = driver.find_element_by_id("app.an10.ito.dev:id/btnSingle").click()
driver.find_element_by_id("app.an10.ito.dev:id/cbTaggingAsset").click()
driver.find_element_by_id("app.an10.ito.dev:id/btnScanSamartTag").click()
time.sleep(5)
driver.find_element_by_id("app.an10.ito.dev:id/ivQrCodeSuccess").click()
for i in range(1,3):
    #time.sleep(2)
    driver.find_element_by_id("app.an10.ito.dev:id/fbAddChildAssetImages").click()
    #time.sleep(2)
    driver.find_element_by_id("app.an10.ito.dev:id/buttonCapture").click()
    #time.sleep(2)
    driver.find_element_by_id("app.an10.ito.dev:id/buttonOK").click()
driver.find_element_by_id("app.an10.ito.dev:id/btnSubmitChildAsset").click()
driver.find_element_by_id("app.an10.ito.dev:id/btnNextParentAsset").click()
driver.find_element_by_id("app.an10.ito.dev:id/btnNextManufacture").click()
driver.find_element_by_id("app.an10.ito.dev:id/btnFinish").click()
if driver.find_element_by_id("app.an10.ito.dev:id/tvAssetManagement").is_displayed():
    print("test pass")
else:
    print("test fail")



