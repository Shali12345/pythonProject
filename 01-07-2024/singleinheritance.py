class Father:
    key= "abc"
    def BHK2(self):
        print("I have 2 BHK")


class child(Father):
    def BHK3(self):
        print("I have 3 bhk")

child_ref=child()
child_ref.BHK3()
print(child_ref.key)
child_ref.BHK2()
