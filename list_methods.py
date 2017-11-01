names = ['Chris', 'Katie',]
names.append('Chelsea')
print(names)


#removes last thing from list and returns it
first_index = names.pop(0)
print(names)
print(first_index)

del names[0]
print(names)

names.insert(0, "Joe")
#index and 'object' being added to list
print(names)
var = "Lauren"
names.insert(0, var)
print(names)
