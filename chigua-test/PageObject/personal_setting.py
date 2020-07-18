#coding=utf-8
from common.BasePage import AppiumOperate
from appium.webdriver.common.mobileby import MobileBy

class PersonalSetting(AppiumOperate):
    loginout_button = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/btn_exit_login")
    loginout_button1 = (MobileBy.XPATH,"//android.widget.Button[@text='退出登录']")
    sure_login = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_common_dialog_left_btn")
    #sure_login = (MobileBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[1]")
    login_frame = (MobileBy.ID,"android:id/content")




    def click_loginout(self):
        self.click(*self.loginout_button)

    def click_sure_loginout(self):
        self.click(*self.sure_login)

    def switch_login_frame(self):
        self.switch_to_frame(*self.login_frame)

    def move_to_surelogin(self):
        self.move_to(*self.sure_login)
