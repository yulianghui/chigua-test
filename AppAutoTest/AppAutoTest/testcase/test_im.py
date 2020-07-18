#coding=utf-8
import os
#coding=utf-8
import unittest
from common import BasePage
from time import sleep
from PageObject.loginpage import LoginPage
from PageObject.personal_setting import PersonalSetting
from PageObject.personcenter import PersonCenter
from appium.webdriver.common.mobileby import MobileBy
from PageObject.impage import Impage
from common.common import Common_method
from PageObject.tabpage import TabPage
from common.driver import DriverClinet
from common.driver import DriverClinet

class Test_im(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        DriverClinet().open_app()
        #cls.driver.launch_app()
        Common_method().login()

    def setUp(self):

        TabPage().click_im()

    def test_message(self):
        print("测试开始")


    @classmethod
    def tearDownClass(cls):
        common = Common_method()
        common.loginout(Impage().im_person_image)
        """
        f = os.popen(r"adb shell dumpsys activity top | findstr ACTIVITY", "r")  # 获取当前界面的Activity
        current_activity = f.read()
        f.close()
        #print(current_activity)  # cmd输出结果

        # 用in方法 判断一个字符串是否包含某字符
        apppackage_name = 'com.dianyou.app.market.activity.MainTabActivity'
        """
        driver = DriverClinet()
        driver.close_app()





