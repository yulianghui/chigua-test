#coding=utf-8
import unittest
from common import BasePage
from time import sleep
from PageObject.loginpage import LoginPage
from PageObject.personal_setting import PersonalSetting
from PageObject.personcenter import PersonCenter
from appium.webdriver.common.mobileby import MobileBy
from common.common import Common_method
from common.driver import DriverClinet
from common.driver import DriverClinet
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
ding = utf-8



class Cla(unittest.TestCase):


    a=1
    b=2

    def test_add(self):

        c = self.a + self.b
        self.assertEqual(c,3,"计算错误")
"""


class test_LoginApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #driver = .get_driver()
        #cls.driver = DriverClinet().get_driver()
        """
        cls.login = LoginPage()
        cls.common = Common_method()
        cls.personcenter = PersonCenter()
        cls.personsetting = PersonalSetting()
        
        """
        DriverClinet().open_app()
        print("登录测试开始")
    def setUp(self):

        #self.test = BasePage.AppiumOperate()
        self.common = Common_method()
        self.personcenter = PersonCenter()
        self.personsetting = PersonalSetting()



    def test01_login(self):
        """
        #self.login = LoginPage()

        #self.login = LoginPage()
        #self.test.find_by_id('com.dianyou.app.market.dyclient:id/dianyou_red_envelope_login_cl').click()
        self.login.find_element(MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_red_envelope_login_cl").click()
        self.login.input_username("19999999999")
        self.login.input_password("abc123456")
        self.login.click_box()
        sleep(1)
        self.login.click_login()
        sleep(3)


        #self.test.openredpag_click()

        self.login.redppagtoast()
        self.login.redpack_rain()


        #self.login = Common_method().login()
        a = self.login.find_element(*self.login.yesterday_toast_loc).is_displayed()
        self.assertTrue(a)
        self.login.yesterday_toast_click()
        """
        Common_method().login()
    def test02_loginout(self):
        """
        #self.personcenter = PersonCenter()
        #self.personsetting = PersonalSetting()


        PersonCenter().click_personimage()
        PersonCenter().click_setting()
        PersonalSetting().click_loginout()

        PersonalSetting().move_to_surelogin()
        PersonalSetting().click_sure_loginout()
        sleep(3)
        """
        self.loginout = self.common.loginout(self.personcenter.personimage)

        text = self.personcenter.myname_text()
        print(text)
        self.assertEqual(text,"请登录")

    @classmethod
    def tearDownClass(cls):

        driver = DriverClinet()
        driver.close_app()



        print("测试结束")



