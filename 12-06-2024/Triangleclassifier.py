side1= int(input("Enter side 1 of triange"))
side2= int(input("Enter side 2 of triange"))
side3= int(input("Enter side 3 of triange"))
if side1==side2==side3:
  print("Equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
  print("Isosceles triangle")
else:
  print("Scalene triangle")