#anytime you're thinking about returning a list from a function
#you can return a generator
#the output items are calculated as needed
#range is the mathematical promise of integers, that's really
#a generator
#this calculates it only when we need it
#it's better on memory

def gen_odd_num(less_than):
    for x in range(less_than):
        if x % 2 == 1:
            yield x
#yield
print(gen_odd_num(101))

for i in gen_odd_num(101):
    print(i)

#we cannot index a generator
