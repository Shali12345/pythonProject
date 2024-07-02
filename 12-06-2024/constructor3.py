class VWOLogin:
    email= None  #optional
    password= None #optional

    def __init__(self,email_arg,password_arg):
        self.email= email_arg
        self.password= password_arg


    def login_confirm(self):
        if self.email=="shalini@gmail.com" and self.password=="123":
            print("Allowed")

        else:
            print("Not allowed")


amit= VWOLogin("amit@gmail.com","wer")
amit.login_confirm()

shalini=VWOLogin("shalini@gmail.com", "123")
shalini.login_confirm()