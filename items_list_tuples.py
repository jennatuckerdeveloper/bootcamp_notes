my_dict = {'key1' : 'value1', 'key2' : 'value2'}

#print(type(my_dict.items()))
#returns:  <class 'dict_items'>
#dict_items is it's own thing, and that thing is not idexable
#the rest of the code converts the dict_items into something idexable
#by turning it into a list

#print(my_dict.items()[0])
#returns:  TypeError: 'dict_items' object does not support indexing
print(list(my_dict.items()))
print(list(my_dict.items())[0])
print(list(my_dict.items())[0][0])
print(list(my_dict.items())[0][1])

variable = ('2015', '8573226')
