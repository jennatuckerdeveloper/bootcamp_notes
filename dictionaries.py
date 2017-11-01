name_of_dictionary = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3'
}
#the key in a dictionary needs to be something that is HASHABLE
print(name_of_dictionary['key1'])
print(name_of_dictionary.keys())

#you can use an interger for a key, that's fine
#hasable means immutable, unchangeable, the computer knows what it is
#and it has a set definiton
name_of_dictionary["key4"] = "value 4"
print(name_of_dictionary)

del name_of_dictionary["key1"]
print(name_of_dictionary)

#dict.items() to iterate through a dictionary 
