
# father has multiple children
class Father:
    key= "abc"
    def BHK2(self):
        print("I have 2 BHK")

class Amit(Father):
    def BHK4(self):
        print("I have 4 BHK")

class Sorab(Father):
    def BHK3(self):
        print("I have 3 bhk")



amit= Amit()
amit.BHK4()
amit.BHK2()
print(amit.key)

#amit.BHK3()- not possible

sorab=Sorab()
sorab.BHK3()
sorab.BHK2()
print(sorab.key)

#sorab.BHK4()- not possible