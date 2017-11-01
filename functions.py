#build a block of code that will excute whenever we tell it to execute

def my_function_name(name):
    print("Hello, {}!".format(name))

my_function_name("Jen")

#we mainly want functions to do only ONE thing but do ONE thing WELL
#if you need the funciton to do more things, then make more functions
#and have them call those "earlier" functions
#that makes debugging much easier

#you'll typically not use print as the final command, you'll use return
#you'll put the print command where you run the function if you want it printed
#you can assign the output (what's returned) to a variable
#then you can print that variable or work with it otherwise
