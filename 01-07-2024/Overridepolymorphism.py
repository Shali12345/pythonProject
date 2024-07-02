class Shape:
    def area(self):
        print("area of shape")


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
          return 3.14 * self.radius * self.radius


# shape1 = Rectangle(3,4)
# print(shape1.area())

shape2 = circle(10)
print(shape2.area())

# shape3 = Shape()
# shape3.area()
