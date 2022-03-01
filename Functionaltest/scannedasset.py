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
#driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup").click()
'''
inputA = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((MobileBy.ID, "app.an10.ito.dev:id/btnSignIn"))
)
inputA.click()
#time.sleep(10)
inputB = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((MobileBy.ID, "app.an10.ito.dev:id/tvEmail"))
)
inputB.send_keys("maavuz")
inputc = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((MobileBy.ID, "app.an10.ito.dev:id/tvPassword"))
)
inputc.send_keys("test123")
driver.hide_keyboard()
#inputB.clear()


inputd = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((MobileBy.ID, "app.an10.ito.dev:id/btnLogin"))
)
inputd.click()
#time.sleep(10)
'''
driver.find_element_by_accessibility_id("Open navigation drawer").click()
driver.find_element_by_id("app.an10.ito.dev:id/tvScannedAsset").click()
driver.find_element_by_id("app.an10.ito.dev:id/tvScannedAsset").click()

state= driver.find_element_by_id("app.an10.ito.dev:id/textViewSyncState")
state.text
if state.text=="Not Synced":
    driver.find_element_by_id("app.an10.ito.dev:id/btnSync").click()
driver.find_element_by_accessibility_id("Navigate up").click()
driver.find_element_by_id("app.an10.ito.dev:id/tvScannedAsset").click()

state= driver.find_element_by_id("app.an10.ito.dev:id/textViewSyncState")
state.text
if state.text=="Created":
    driver.find_element_by_id("app.an10.ito.dev:id/imageViewDelete").click()
else:
    print("testfail")

#again_state=driver.find_element_by_id("app.an10.ito.dev:id/textViewSyncState")
#again_state.text


