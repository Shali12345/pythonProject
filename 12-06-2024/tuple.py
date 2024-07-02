# Conversion of list into tuple

t1= tuple(["hello","hi", "namo"])
print(t1)

# deletion of tuple
del t1
#print(t1)


# tuple containing tuple
hero1=("Batman", "Bowler")
hero2=("Batman1", "Bowler1")
new_tuple=(hero1,hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[0][0])
print((new_tuple[0][1]))

# use of "in" to find item in tuple
cities= ("Paris","delhi","goa")
print("Paris"in cities)
print("new delhi"in cities)

# to add something in tuple-concatenation
t= (12,13,14,15)
new_t= t+(3,)
print(new_t)

#replication
new_t= t*2
print(new_t)