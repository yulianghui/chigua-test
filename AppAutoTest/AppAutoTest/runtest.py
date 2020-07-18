#coding=utf-8

import time
from module import *

from testcase import testcase_path
from test_report import testReport_path
from test_report.HTMLTestRunner import HTMLTestRunner
from common.driver import DriverClinet

if __name__ == "__main__":
    test_dir = testcase_path.dir_path()

    report_dir = testReport_path.report_path()

    now = time.strftime("%Y-%m-%d")
    filename = report_dir + '\\report-' + now +'.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,title='UI自动化测试报告',description='用例执行情况',verbosity=2)
    runner.run(getTestcases.testcaseDir(test_dir))
    driver = DriverClinet()
    driver.quit_app()
    fp.close()
    time.sleep(3)
    result = getTestResult.get_result(filename)
    print ("用例执行情况：%s"%result)

    mail = sendEmail.send_Email(filename,result)
    """
    if mail:
        print ('邮件发送成功')
    else:
        print("邮件发送失败")

    """