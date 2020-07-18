#coding=utf-8

from common.BasePage import AppiumOperate
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(AppiumOperate):
    """
    username_id ="com.dianyou.app.market.dyclient:id/et_phone"
    password_id = "com.dianyou.app.market.dyclient:id/et_pwd"
    agreement_id = "com.dianyou.app.market.dyclient:id/ck_user_protocol"
    submit_id = "com.dianyou.app.market.dyclient:id/btn_login"
    redpackageopen_id = 'com.dianyou.app.market.dyclient:id/dianyou_red_envelope_dialog_open'
    text_xpath = "//*[contains(text(),'昨日收入(GZ)')]"
    """
    username_loc = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/et_phone")
    password_loc = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/et_pwd")
    agreement_loc = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/ck_user_protocol")
    submit_loc = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/btn_login")
    redpackageopen_loc = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_red_envelope_dialog_open")
    yesterday_toast_loc  = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/ec_wallet_yesterday")


    def input_username(self,username):

        #self.find_by_id(id=self.username_id).clear()
        #self.find_by_id(self.username_id).send_keys(username)
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self,password):
        #self.find_by_id(self.password_id).clear()
        #self.find_by_id(self.password_id).send_keys(password)
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def click_box(self):
        #self.find_element(*self.agreement_loc).click()
        self.click(*self.agreement_loc)

    def click_login(self):
        #self.find_by_id(self.submit_id).click()
        self.find_element(*self.submit_loc).click()

    def openredpag_click(self):
        #self.find_by_id(self.redpackageopen_id).click()
        self.find_element(*self.redpackageopen_loc).click()

    def yesterday_toast_click(self):
        self.find_element(*self.yesterday_toast_loc).click()