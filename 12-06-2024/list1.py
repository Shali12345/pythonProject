numbers= [1,2,3]
# during defining function, argument name can be anything, but during calling function argument name should be correct as initiliazed
def do_something(shalini_list):
    shalini_list.append(5)
    shalini_list[2]=45
    return shalini_list


l=do_something(numbers)
print(l)

# copy list
copy_list=numbers.copy()
print(copy_list)