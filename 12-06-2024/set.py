set1= {1,2,3,4,4,5}

for i in set1:
    print(i)
print(set1)

set2={4,5,6,7,8}

#convert list into set
list1= [1,2,3,4]
set1= set(list1)
print(set1)

# union
my_set= set1.union(set2)
print(my_set)

#intersect
my_set=set1.intersection(set2)
print(my_set)

#difference
my_set= set1.difference(set2)
print(my_set)

# difference
my_set= set2.difference(set1)
print(my_set)