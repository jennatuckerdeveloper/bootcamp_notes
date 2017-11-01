#if you don't know how many arguments you want to take:
#you use *args **kwargs (key word argument) comes in as a
#key-value pair
def make_tuple(*args):
    print(args) #you don't use the asterix

make_tuple("the", "cat", "in", "the", "hat")

def make_list_of_strings(*args):
    lst = (list(args)) #you don't use the asterix
    #make the output a variable, so you can use it later
    thing1 = lst.pop()
    print(thing1)

print(make_list_of_strings("the", "cat", "in", "the", "hat"))

def make_list_of_strings(*args):
    return (list(args)) #you don't use the asterix

lst = make_list_of_strings("the", "cat", "in", "the", "hat")
print(lst)
