#list comprehensions, you can build a list out of an iterator
names = ['Jen', 'Joe', 'Tim']
lower_names = [i.lower() for i in names]
print(lower_names)
#obviously, i could be anything, it's just a variable name
#oddly, you say what you want to do to the variabe bf you do it

#you can use a function with a list comprehension

#This does the same thing as:
lower_names_2 = []
for name in names:
    lower_names_2.append(name.lower())

print(lower_names_2)

print([num for num in range(101)])
print([num for num in range(101) if num % 2 == 0])
#so you can't use an elif and else

years = [1995, 2000, 2004, 2011]
leap_years = [year for year in years if year % 4 == 0]
# year is the thing we're iterating
#x for x in years, if x
#i for i in years, if x
print(leap_years)  #> [2000, 2004]
#Python is open source.  Anyone can contribute to Python.
#Chris says, they're not particulary easy to read.
#That makes them not particuarly Pythonic.  Python is usually
#made to be easy for humans to read.
