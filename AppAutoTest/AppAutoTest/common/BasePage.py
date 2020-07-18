#coding=utf-8
from appium import webdriver

from common.driver import DriverClinet
from time import sleep
from screeshot import getScreeshot_path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time


class AppiumOperate(object):

    def __init__(self):
        self.screeshot_path = getScreeshot_path.screeshot_path()

        at = DriverClinet()
        self.driver = at.get_driver()
        #self.implicitly_wait(10)

        #self.driver.find_element_by_id('book_button_close').click()
        #self.driver = driver


    #
    def get_screen(self):
        now = time.strftime("'%Y-%m-%d %H:%M:%S'")
        filename = self.screeshot_path + '\\screeshot-' + now + '.png'
        self.driver.get_screenshot_as_file(filename)


    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素"%(self, loc))

    #红包弹窗
    def redppagtoast(self):

        try:
            loc = ('id',"com.dianyou.app.market.dyclient:id/dianyou_red_envelope_dialog_open")
            e=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))

            e.click()

        except:
            pass

    #红包雨弹窗
    def redpack_rain(self):
        try:
            loc = ('id', "com.dianyou.app.market.dyclient:id/confirm")
            e = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))

            e.click()

        except:
            pass


    def close_app(self):
        self.driver.quit()


    def get_text(self,*loc):
        try:
            text=self.find_element(*loc).text
            return text
        except:
            print(u"%s 页面中未能找到 %s 元素"%(self, loc))

    def click(self,*loc):
        try:
            el = self.find_element(*loc)
            el.click()
            #self.find_element(*loc).click()

        except:
            print(u"%s 页面中未能找到 %s 元素"%(self, loc))

    def send_keys(self,*loc,text):
        try:
            el = self.find_element(*loc)
            el.send_keys(text)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def submit(self,*loc):
        try:
            return self.find_element(*loc).submit()

        except:
            print(u"%s 页面中未能找到 %s 元素"%(self, loc))

    def move_to(self,*loc):
        #鼠标移动
        try:
            el = self.find_element(*loc)
            return ActionChains(self.driver).move_to_element(el).perform()
        except:
            print(u"%s 页面中未能找到 %s 元素"%(self, loc))

    def right_click(self,*loc):
        #鼠标右键点击
        try:
            el = self.find_element(*loc)
            return ActionChains(self.driver).context_click(el).perform()
        except:
            print(u"%s 页面中未能找到 %s 元素"%(self, loc))

    def double_click(self,*loc):
        #鼠标双击
        try:
            el = self.find_element(*loc)
            return ActionChains(self.driver).double_click(el).perform()
        except:
            print(u"%s 页面中未能找到 %s 元素"%(self, loc))

    def count_elements(self,*loc):
        #元素个数
        try:
            els = self.find_element(*loc)
            return len(els)
        except:
            print(u"%s 页面中未能找到 %s 元素"%(self, loc))


    def drag_element(self,source,target):

        #拖动元素

        el1 = self.find_element(source)
        el2 = self.find_element(target)
        return ActionChains(self.driver).drag_and_drop(el1,el2).perform()

    def get_selected_text(self,*loc):
        """
          获取 Select 元素的选择的内容
          :param selector: 选择字符 "i, xxx"
          :return: 字符串
          """
        el = self.find_element(*loc)
        selected_opt = Select(el).first_selected_option()
        return selected_opt.text

    def select_by_visible_text(self, *loc, text):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        #根据文本取消下拉框选择
        el = self.find_element(*loc)
        Select(el).select_by_visible_text(text)

    def select_by_value(self,*loc,value):
        #选择下拉框选择
        el = self.find_element(*loc)
        Select(el).select_by_value(value)

    def execute_js(self,script):
        #操作js
        return self.driver.execute_script(script)

    def get_value(self,*loc):
        #获取元素的值
        el = self.find_element(*loc)
        return el.get_attribute("value")

    def get_attribute(self,*loc,attribute):
        #获取元素的值
        el = self.find_element(*loc)
        return el.get_attribute(attribute)

    def get_displayed(self,*loc):
        #获取元素是否可见，返回Ture或者False
        el = self.find_element(*loc)
        return el.is_displayed()

    def get_exist(self,*loc):
        #判断元素是否存在，返回Ture或者False
        flag = True
        try:
            self.find_element(*loc)
            return flag

        except:
            flag = False
            return  flag

    def get_enabled(self,*loc):
        #判断元素是否可点击
        el = self.find_element(*loc)
        if el.is_enabled():
            return  True
        else:
            return False

    def get_title(self):
        #获取页面标题
        return self.driver.title

    def get_url(self):
        #获取页面地址
        return self.driver.current_url

    def get_selected(self,*loc):
        #判断元素是否被选中，返回bool类型
        el = self.find_element(*loc)
        return el.is_selected()

    def get_text_list(self,*loc):
        #获取元素text列表，返回列表
        el_list = self.find_element(*loc)
        results = []
        for el in el_list:
            results.append(el.text)
        return results

    """
    弹出窗口相关方法
    * 如果弹框的元素可以F12元素查看，则直接使用点击，获取元素等方法
    * 如果弹框元素无法查看，则使用如下方法可以搞定
    """
    def accept_alert(self):
        '''
            Accept warning box.

            Usage:
            driver.accept_alert()
            '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismissAlert()
        '''
        self.driver.switch_to.alert.dismiss()

    def get_alert_text(self):
        '''
        获取 alert 弹出框的文本信息
        :return: String
        '''
        return self.driver.switch_to.alert.text

    def text_in_alert(self,text):
        '''在prompt对话框内输入内容'''
        self.driver.switch_to.alert.send_keys(text)
        #self.forced_wait(1)

    def alert_new_display_none(self,selector_by_id_value):
        '''
        使用 JS 处理新型弹出框
        :param selector_by_id_value: id方式定位弹出框(div)的 value 值
        :return: 无
        '''
        js = 'document.getElementById("%s").style.display="none";' %selector_by_id_value
        self.driver.execute_script(js)


    def switch_to_frame(self,*loc):
        #切换框架
        el = self.find_element(*loc)
        return self.driver.switch_to_frame(el)

    def switch_to_defaultframe(self):
        #切换回默认框架
        return self.driver.switch_to_default_content()

    def switch_to_window_by_title(self, title):
        '''
            切换不同页面窗口
        '''
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                break

            self.driver.switch_to.default_content()

    def explicitly_wait(self, selector, seconds):
        """
        显式等待
        :param selector: 定位字符
        :param seconds: 最长等待时间，秒
        :return:
        """
        locator = self.find_element(selector)

        WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located(locator))

    def implicitly_wait(self, seconds):
        """
        Implicitly wait. All elements on the page.
        :param seconds 等待时间 秒
        隐式等待

        Usage:
        driver.implicitly_wait(10)
        """
        self.driver.implicitly_wait(seconds)

    def upload_input(self,*loc,file):
        '''
                上传文件 （ 标签为 input 类型，此类型最常见，最简单）
                :param loc: 上传按钮定位
                :param file: 将要上传的文件（绝对路径）
                :return: 无
                '''


        self.find_element(*loc).send_keys(file)

    """
    def download(self,download_path,file_type,*download_loc):
        '''
            下载（设置指定下载路径，不用每次都弹出对话框选择保存路径）
            :param download_path: 设置默认下载路径
            :param file_type: 默认下载文件类型
            :param download_selector: 下载元素定位
            :return:
            '''
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir', download_path)
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')

        driver = webdriver.Firefox(firefox_profile=profile)
    """

    def swipe(self,start_x, start_y, end_x, end_y, duration=None):

        """
        滑动屏幕
        :param start_x: x轴开始坐标
        :param start_y: y轴开始坐标
        :param end_x: x轴结束坐标
        :param end_y: y轴结束坐标
        :param duration: 滑动所用时间
        :return:
        """

        try:
            return self.driver.swipe(start_x,start_y,end_x,end_y,duration)

        except:
            self.get_screen()
            print("滑动屏幕失败")

















