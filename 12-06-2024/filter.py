numbers= [1,2,3,4,5,6,]

def is_even(num):
    return num%2==0


new_list= filter(is_even, numbers)
print(list(new_list))