#coding=utf-8

import os
#获取测试报告路径
#获取测试报告路径
def report_path():
    return os.path.split(os.path.realpath(__file__))[0]