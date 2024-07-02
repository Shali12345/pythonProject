class Car:
    name= None
    password="123"

    def __init__(self):
        print("I am called when object is created")

    def change_password(self):
        self.password= "234"

xuv= Car()
# xuv.password= "345"  ## this is not allowed