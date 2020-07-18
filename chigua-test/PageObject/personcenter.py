#coding=utf-8

from common.BasePage import AppiumOperate
from appium.webdriver.common.mobileby import MobileBy

class PersonCenter(AppiumOperate):
    personimage = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/red_envelope_home_photo_pb")
    my_wallet = (MobileBy.XPATH,"//android.widget.TextView[@text = '我的钱包']")
    my_gift = (MobileBy.XPATH,"//android.widget.TextView[@text = '我的礼物'")
    my_dynamic = (MobileBy.XPATH, "//android.widget.TextView[@text = '我的动态'")
    my_history = (MobileBy.XPATH, "//android.widget.TextView[@text = '浏览历史'")
    my_activity = (MobileBy.XPATH, "//android.widget.TextView[@text = '活动中心'")
    my_class = (MobileBy.XPATH, "//android.widget.TextView[@text = '吃瓜课堂'")
    my_rule = (MobileBy.XPATH, "//android.widget.TextView[@text = '吃瓜法规'")
    join_team = (MobileBy.XPATH, "//android.widget.TextView[@text = '加入亲友团'")
    my_headphoto = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_game_my_iv_head")
    my_tv_name = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_game_my_tv_name")
    my_nologin_name = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_game_my_tv_name")
    my_tv_id = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_game_my_tv_id")
    my_tv_sign = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_game_my_tv_sign")
    business_loc = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/business")
    qr_icon_loc = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/qr_icon")
    setting_loc = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_game_my_tv_settings")
    help_loc = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_game_my_tv_help")
    feedback_loc = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_game_my_tv_feedback")
    personcenter_frame = (MobileBy.ID,"com.dianyou.app.market.dyclient:id/dianyou_game_main_nav_view")






    def click_personimage(self):
        self.click(*self.personimage)

    def click_setting(self):
        self.click(*self.setting_loc)

    def myname_text(self):
        return  self.get_text(*self.my_nologin_name )

