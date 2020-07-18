#coding=utf-8

from common.BasePage import AppiumOperate

from PageObject.personcenter import PersonCenter
from PageObject.personal_setting import PersonalSetting
from PageObject.loginpage import LoginPage
from appium.webdriver.common.mobileby import MobileBy
from time import sleep


class Common_method(AppiumOperate):



    def login(self):
        login = LoginPage()
        # self.test.find_by_id('com.dianyou.app.market.dyclient:id/dianyou_red_envelope_login_cl').click()
        login.find_element(MobileBy.ID, "com.dianyou.app.market.dyclient:id/dianyou_red_envelope_login_cl").click()
        login.input_username("19999999999")
        login.input_password("abc123456")
        login.click_box()
        sleep(1)
        login.click_login()
        sleep(3)

        # self.test.openredpag_click()
        login.redppagtoast()
        login.redpack_rain()

        #a = self.login.find_element(*self.login.yesterday_toast_loc).is_displayed()
        #self.assertTrue(a)
        login.yesterday_toast_click()


    def loginout(self,loc):
        # self.personcenter = PersonCenter()
        # self.personsetting = PersonalSetting()

        #PersonCenter().click_personimage()
        self.click(*loc)
        PersonCenter().click_setting()
        PersonalSetting().click_loginout()

        PersonalSetting().move_to_surelogin()
        PersonalSetting().click_sure_loginout()
        sleep(3)

