import datetime

class User(object):
    def __init__(self,username,usertype, password, time):
        self.user={}

    def create_user(self,id,name,password,usertype,time):
        self.user[id]= id
        self.user[name]= name
        self.user[password]= password
        self.user[usertype]= usertype
        self.user[time]=datetime.datetime.utcnow()   

    def login_user(self,id,name,password):
        self.user[id]= id
        self.user[name]= name
        self.user[password]= password
