#coding:utf-8
from morequest import Morequest

login_postdata = {"project_id" : "1111563340","project_secret" : "e3ceb5881a0a1fdaad01296d7554868d",
                  "equipId" : "lymon123456","loginType" : "0","username" : "18627245615","response_type" : "post",
                  "userpwd" : "1qaz2wsx","checkFlag" : "true"}

class login_oauth(Morequest):
    def is_err(self):
        login_res = login_oauth.web_post()

        return login_res

    def is_active(self):
        status = "1"
        return status



login_oauth = login_oauth("1","http://120.26.234.189/tgoauth2/authorize!login",login_postdata)
res = login_oauth.is_err()
print res