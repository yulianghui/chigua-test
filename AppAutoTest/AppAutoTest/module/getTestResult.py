#coding=utf-8

from selenium import  webdriver
from time import sleep

#打印测试结果
def get_result(filename):
    driver = webdriver.Chrome()
    driver.maximize_window()
    result_url = "file://%s"%filename
    driver.get(result_url)
    sleep(3)
    res = driver.find_element_by_xpath("/html/body/div[1]/p[3]").text
    result = res.split(':')
    #driver.quit()
    return result[-1]