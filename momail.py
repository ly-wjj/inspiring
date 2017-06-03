import smtplib
import conf
import string
from email.mime.text import MIMEText
from email.header import Header
import recivers



sender="tgopt@timevale.com"
receivers="ly@timevale.com"
subject="test"
message="hello world,test!"
content="hhhhhhhhh"
type="plain"

class Momail():
    def __init__(self,subject,content,type):
        self.host=conf.getConfig("email","host")
        self.port=conf.getConfig("email","port")
        self.user=conf.getConfig("email","user")
        self.password = conf.getConfig("email", "password")
        self.sender = conf.getConfig("email","sender")
        self.receivers = conf.getConfig("email","receivers").split(',')
        self.subject = subject
        self.content = content
        self.type = type
        self.message = MIMEText(self.content, self.type, 'utf-8')
        self.message['From'] = Header('workmonitor', 'utf-8')
        self.message['To'] = Header('optgroup', 'utf-8')
        self.message['Subject'] = Header(self.subject, 'utf-8')

    def sendmail(self):
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.host,self.port)
            smtpObj.starttls()
            smtpObj.login(self.user,self.password)
            smtpObj.sendmail(self.sender,self.receivers,self.message.as_string())
        except smtplib.SMTPException:
            print "Error: can not send email!"



class Mobilemail():
    def __init__(self,item,errcode,apitype,listener):
        self.item = item
        self.errcode = errcode
        self.apitype = apitype
        self.url = conf.getConfig("mobile","url")

    def callmail(self):
        recevier = receivers()
        mobile = receiver.mobile







semail = Momail(subject,content,type)
semail.sendmail()

