def sum_numbers(a, b):
    return a + b


s=sum_numbers(4, 5)
print(s)


# using lambda- execute same code in one line

sum_numbers=lambda a,b: a+b
print(sum_numbers(3,4))

# even_odd

even_odd= lambda num: "Even" if num%2==0 else "ODD"
print(even_odd(5))


# power function
power_function= lambda num: num**3
print(power_function(4))

# input with lambda
power_function= lambda :int(input("Enter number"))**2
result=power_function()
print(result)