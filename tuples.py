#anything in between parentheses ()
tup = ('Chris', ['Jeff', 'Max'], 'Chelsea', 'Katie')
print(tup)
#tuples are immutable
#you might make them when you need something protected / unchangeable
#you CAN change the list that's inside the tuple
#the list is mutable
tup[1].pop(-1)
print(tup)
#you wouldn't be able to use pop on the other indexes
print(len(tup))
