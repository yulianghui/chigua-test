#coding=utf-8

import  smtplib
import  baseinfo
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def send_Email(file_new,result):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    try:
        smtp = smtplib.SMTP(baseinfo.Smtp_Server,25)
        sender = baseinfo.Smtp_Sender
        password = baseinfo.Smtp_Sender_Password
        #receiver = baseinfo.Smtp_Receiver
        receiver = ",".join(baseinfo.Smtp_Receiver)
        smtp.login(sender,password)
        msg = MIMEMultipart()
        text = MIMEText(mail_body,'html','utf-8')
        text['Subject']=Header('UI自动化测试报告','utf-8')
        msg.attach(text)

        now = time.strftime("%Y-%m-%d")
        msg['Subject'] = Header('[执行结果:' + result + ']' + 'UI自动化测试报告' + now ,'utf-8')
        msg_file = MIMEText(mail_body,'html','utf-8')
        msg_file['Content-Type'] = 'application/octet-stream'
        msg_file['Content-Disposition'] = 'attachment;filename="TestReport.html"'
        msg.attach(msg_file)

        msg['From'] = sender
        msg['To'] =receiver
        tmp = smtp.sendmail(sender,receiver,msg.as_string())
        print (tmp)
        smtp.quit()
        return True

    except smtplib.SMTPException as e:
        print (str(e))
        return False
