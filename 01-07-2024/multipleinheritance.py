class A:
    def method(self):
        print("Method A")


class B:
    def method(self):
        print("method B")


class C(A, B):
    pass



c = C()
c.method()  # it will call method of calls A bcz A is written first

# If calls C has method then it will call method of class C bcz local has preferences
