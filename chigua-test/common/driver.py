#coding=utf-8
from appium import webdriver
import os
from screeshot import getScreeshot_path
#from AppiumLibrary.utils import ApplicationCache
"""

class AppiumTest():
    def __init__(self):

        desired_caps = {
            'platformName': 'Android',
            "platformVersion": "7.1.2",
            "deviceName": "127.0.0.1:21503",
            "appPackage": "com.dianyou.app.market.dyclient",
            "appActivity": "com.dianyou.app.market.activity.MainTabActivity"

        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)
        #self.driver.implicitly_wait(30)

    def get_driver(self):
        return self.driver

"""

class Driver_configure(object):
    def __new__(cls, *args, **kw):
        """
        使用单例模式将类型设置为运行时只有一个实例，
        在其他python类中使用基类时，
        可以创建多个对象，保证所有的对象都基于一个浏览
        :param args:
        :param kw:
        :return:
        hasattr()函数功能用来检测对象object中是否含有名为**的属性，
        如果有就返回True，没有就返回False
        """
        if not hasattr(cls, '_instance'):
            orig = super(Driver_configure, cls)
            desired_caps = {}
            desired_caps['platformName'] = 'Android'  # 平台
            desired_caps['platformVersion'] = '7.1.2'  # 平台版本
            # self.desired_caps['app'] = '***1.apk'   # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
            desired_caps['appPackage'] = "com.dianyou.app.market.dyclient"  # APK包名
            # cls.desired_caps['appActivity'] = '.ui****tivity'
            # 被测程序启动时的Activity  .'activity名，可以通过appium的inspection找到该名称'
            desired_caps['appActivity'] = 'com.dianyou.app.market.activity.MainTabActivity'
            # self.desired_caps['appActivity'] = 'com**ding_Activity'
            desired_caps['unicodeKeyboard'] = 'true'  # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
            desired_caps['resetKeyboard'] = 'true'  # 是否在测试结束后将键盘重轩为系统默认的输入法。
            desired_caps['newCommandTimeout'] = '120'  # Appium服务器待appium客户端发送新消息的时间。默认为60秒  # 超时时间
            desired_caps['deviceName'] = "127.0.0.1:21503"
            # 手机ID(adb devices可获得)
            #desired_caps['noReset'] = True  # true:不重新安装APP，false:重新安装app
            # noReset的意思是，每次启动APP不清除之前的状态，如登录后重新启动session时不需要再次登录，保留之前的登录状态
            # cls.desired_caps['autoGrantPermissions'] = True
            # self.desired_caps['noSign'] = True
            # 远程控制，通过appium可设置；若是真机，直接填写http://localhost:4723/wd/hub 或者http://127.0.0.1:4723/wd/hub即可
            cls._instance = orig.__new__(cls)
            cls._instance.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return cls._instance


class DriverClinet(Driver_configure):

    def get_driver(self):
        return self.driver
    def close_app(self):
        at = self.get_driver()
        at.close_app()

    def open_app(self):

        f = os.popen(r"adb shell dumpsys activity top | findstr ACTIVITY", "r")  # 获取当前界面的Activity
        current_activity = f.read()
        f.close()
        #print(current_activity)  # cmd输出结果

        # 用in方法 判断一个字符串是否包含某字符
        apppackage_name = 'com.dianyou.app.market.activity.MainTabActivity'
        if apppackage_name in current_activity:
            pass
        else:
            at = self.get_driver()
            at.launch_app()

    def quit_app(self):
        f = os.popen(r"adb shell dumpsys activity top | findstr ACTIVITY", "r")  # 获取当前界面的Activity
        current_activity = f.read()
        f.close()
        #print(current_activity)  # cmd输出结果

        # 用in方法 判断一个字符串是否包含某字符
        apppackage_name = 'com.dianyou.app.market.activity.MainTabActivity'
        if apppackage_name in current_activity:
            at = DriverClinet().get_driver()
            at.quit()

        else:
           pass



