class father:
    def home(self):
        print("BHK 2")

class Son(father):
    def home(self):
        super().home()  # with the help of super keyword, son can access the house of father also
        print("No house")

f=Son()
f.home()
