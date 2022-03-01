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
#driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup").click()
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
time.sleep(10)
'''

driver.find_element_by_accessibility_id("Open navigation drawer").click()
driver.find_element_by_id("app.an10.ito.dev:id/tvScannedAsset").click()
driver.find_element_by_id("app.an10.ito.dev:id/tvAssetManagement").click()
time.sleep(5)
driver.find_element_by_accessibility_id("tst1010. 5bf64eaff290463aedd03fb2.").click()

time.sleep(5)
driver.tap([(533, 873)])
driver.find_element_by_xpath("//android.support.v7.app.ActionBar.Tab[@content-desc='Inventory']/android.widget.TextView").click()
time.sleep(1)
#driver.find_element_by_id("app.an10.ito.dev:id/imageButton").click()
#driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
#TouchAction(driver).press(x=, y=).wait(3000).move_to(x=, y=).release().perform()
for i in range(1,5):
    loop=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[i]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView" % i)
    print(loop.text)


