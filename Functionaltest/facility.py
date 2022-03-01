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
driver.find_element_by_id("app.an10.ito.dev:id/tvEAMDatabase").click()
#count=0
#for i in range (1,400):
 #   name=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[%d]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView" % i)
 #   print(name.text)
 ##   driver.swipe(714, 1244, 697, 1086, 400)
    #print(count)
   # if i==5:

    #time.sleep(3)
        #action = TouchAction(driver)
        #action.press(x=, y=).move_to(x=, y=).release().perform()

    #    i==1


    #driver.tap([(632, 1548)])
    #d#river.tap([(672, 1423)])
