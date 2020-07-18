#coding = utf-8
"""
from appium import webdriver

desired_caps = {
    'platformName':'Android',
    "platformVersion":"7.1.2",
    "deviceName":"127.0.0.1:21503",
    "appPackage":"com.dianyou.app.market.dyclient",
    "appActivity":"com.dianyou.app.market.activity.MainTabActivity"

}
webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
"""

from selenium import webdriver
from time import  sleep
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
sleep(3)
driver.quit()
