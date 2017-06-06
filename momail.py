import smtplib
import conf
import string
from email.mime.text import MIMEText
from email.header import Header
from receivers import Contacts
from morequest import Morequest




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

    def sendmail(self):
        message = MIMEText(self.content, self.type, 'utf-8')
        message['From'] = Header('workmonitor', 'utf-8')
        message['To'] = Header('optgroup', 'utf-8')
        message['Subject'] = Header(self.subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.host,self.port)
            smtpObj.starttls()
            smtpObj.login(self.user,self.password)
            smtpObj.sendmail(self.sender,self.receivers,message.as_string())
        except smtplib.SMTPException:
            print "Error: can not send email!"



class Mobilemail():
    def __init__(self,item,apitype,errcode,lis_mobile):
        self.item = item
        self.errcode = errcode
        self.apitype = apitype
        self.url = conf.getConfig("mobile","url")
        self.lis_mobile = lis_mobile

    def callmail(self):

        if self.item == "1":
            code = "5"+str(self.apitype)+self.errcode+"000"
        print code

        policy = conf.getConfig("mobile", "policy")
        templateId = conf.getConfig("mobile", "templateId")
        postdata = {"code":code,"mobile":self.lis_mobile,"policy":policy,"templateId":templateId}

        try:
            request = Morequest(self.item,self.item,postdata)
            print self.url
            response =  request.json_post()
            print "call you--------------------------------!"
        except:
            print "callmail error"
#receiver = Contacts()
#lis_mobile = receiver.get_mobile()
#semail = Mobilemail("1","2","0",lis_mobile)
#semail.callmail()

