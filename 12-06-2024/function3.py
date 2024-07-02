# argument+ return
def sum(a=4, b=7):
    return a + b


result = sum(5)
print(result)


# *args

def pizza(*toppings, base):
    print(*toppings, base)


amit = pizza("onion", "capsicum", "jalapeno", base="thin crust")
