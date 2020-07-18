#coding=utf-8

from common.BasePage import AppiumOperate
from appium.webdriver.common.mobileby import MobileBy

class TabPage(AppiumOperate):

    cicle_loc = (MobileBy.XPATH,"//android.widget.LinearLayout[@id = 'com.dianyou.app.market.dyclient:id/dianyou_tab_icon_iv' and @text = '圈子']")
    IM_loc = (MobileBy.XPATH,"//android.widget.LinearLayout/android.widget.TextView[@text = '消息']")
    redpag_loc = (MobileBy.XPATH,"//android.widget.LinearLayout[@id = 'com.dianyou.app.market.dyclient:id/dianyou_tab_icon_iv'] and @text = '红包']")
    life_loc = (MobileBy.XPATH,"//android.widget.LinearLayout[@id = 'com.dianyou.app.market.dyclient:id/dianyou_tab_icon_iv' and @text = '生活圈']")
    redio_loc = (MobileBy.XPATH, "//android.widget.LinearLayout[@id = 'com.dianyou.app.market.dyclient:id/dianyou_tab_icon_iv' and @text = '小视频']")


    def click_cicle(self):
        self.click(*self.cicle_loc)

    def click_im(self):
        self.click(*self.IM_loc)