# key-value pair
dist1= {"name": "shalini", "age": 60, "city": "noida"}
print(dist1)
print(dist1["name"])

# can change the value

dist1["name"]= "shalu"
print(dist1)

# get function

print(dist1.get("age"))

# to print values and keys
print(dist1.values())
print(dist1.keys())

# convert dictionery to list
print(list(dist1.keys()))
print(list(dist1.values()))

# one by one
for i in list(dist1.values()):
    print (i)

    # to take key-value together
    for k,v in dist1.items():
        print(k,v)