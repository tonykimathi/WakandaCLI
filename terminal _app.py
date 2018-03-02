class Comments():
    comment={}

    def __init__(self,username,usertype,password,time,message):
        self.comment[username]=name
        self.comment[password]=password
        self.comment[usertype]=usertype
        self.comment[time]=time
        self.comment[message]=comment

    def create_comments(self):
        self.username=input("enter your username")
        self.password=input("enter your password")
        self.message=input("enter your comment here")
        self.time=datetime.datetime.utcnow()

        return "comment created successfully"


    def edit_comments(self,):
        if username not in self.comment:
            raise ValueError("user does not exist")


        else:
            instance = {
                "message": self.message,
                "time": self.time
                }
        self.comment[username] = instance

        return instance



