n=int(input("Enter number"))
# if num<0:
#     print("Factorial doesn't exist for negative numbers")
# if num==0:
#     print("Factorial of o is 1")
# else:
#     fact=1
#     for i in range(1, num+1):
#         # i will run from 1 to 3 if number is 3
#         fact= fact*i
#         # i=1
#         # fact= 1*1
#         # fact=1
#         # i=2
#         # fact= 1*2
#         #fact=2
#         # i=3
#         # fact=2*3
#         # fact=6
#     print("Factorial", fact)


factorial= 1
while(n>0):
    factorial= factorial*n
    n=n-1

print(factorial)

