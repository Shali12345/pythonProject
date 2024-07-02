class Person:
    # attribute
    name = None
    id = None
    address = None
    phone = None

    # behaviour
    def walk(self):
        print("I can walk")

    def talk(self):
        print("I can talk")

    # object creation

s1 = Person()
s1.name = "Shalini"
s1.walk()
s2 = Person()
s2.id = 1233
s2.talk()
