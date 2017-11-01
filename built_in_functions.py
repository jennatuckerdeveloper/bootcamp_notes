#built-in functions
#some of Chris's commonly used built-in functions
#casters = change something into a data-type, example float
dict()
list()
#example would be turning the substrings of a string into a list
names = ["Chris", "Katie", "Chelsea", "Chris"]
for name in names:
    print(name)
for i in list(range(len(names))):
    print('{}: {}'.format(i, names[i]))
float()

#len is easier on memory than something that stores the list
number = list(range(0, 100))

print(number)
int()
str()
input()
eval() #reads a string as Python code
len()
max()
min()
reversed()
sum()
abs()

#familiarize yourself with the built-in functions
#get a general idea of what they're doing
