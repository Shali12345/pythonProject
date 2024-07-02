class Dog:
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def walk(self):
        print("I am walking",self.name)


Dog1 = Dog("shal", 1)
Dog2 = Dog("sfg", 2)
print(f"{Dog2.name} has ID {Dog2.id}")
Dog1.walk()
