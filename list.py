#lists
#[]
my_list = ['this', 235, 346436.436, ['hey', 'blah']]
print(my_list[0]) #will print 'this'
print(my_list[3][0]) #will print 'hey'
# references first layer of list index, then second
# this is called levels of nesting
# you generally want things flat instead of nested
# so you will want to keep it at only one or two levels of lists
# classes are a better way to tier information

print(my_list[1:3])
#It goes:  start:stop:step
list2 = my_list[1:3]
print(list2)

#print last item from a list
print(my_list[-1])
print (my_list[-1][-1])
#print second from last
print(my_list[-2])

#integers aren't index-able
numbers = list(range(0,101))
print(numbers)
print(numbers[::5]) #step of 5

#print list in reverse
print(numbers[::-1])

#anything that's inex-able:  strings, lists 
