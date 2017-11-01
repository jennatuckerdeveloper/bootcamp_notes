#CLASSES, CLASS OBJECTS, OVERLOADING
#You can package in variables and functions both
#Python class names use CamelCase, but they also capitalize the first word

#This is the most basic way to make a class
class Person:   #you might see:  class Person(object):
    pass

class Person:
    #we're going to give it some initialization arguments
    def __init__(self, name):  #this is the initialization part of the constructor
    #the classes constructing an object have this first
    #you'll usually have this.
    #a function that's inside of a class is called a method
    #self is basically a way for it to self-refer
        self.name = name
        #every method inside of a class needs to take self as it's very first arguments
        #instantiate our class and make an object of Person
    def print_name(self):
        print(self.name)
    #so this is a function
    def __str__(self):
        return 'Person object of {}'.format(self.name)
    #the string method is default to object, so it's inherited
    #we are OVERLOADING this method
    def __repr__(self):
        #return 'Person object of {}'.format(self.name)
        return self.__str__()
        #these two lines of code above do the exact same thing two different ways
chris = Person("Chris")
chris.phone = "374-134-3423"
#so you don't have to enter a perameter for self
chris.print_name()
print(chris.phone)
#I'm still not quite sure why you need self, but it's kind of a standard variable
chris.name = "Christopher"
chris.print_name()
#so you can change / overwrite a variable, no problem
#everything attached to the Class is an attribute
#so the name attribute and the print name function
print(chris)
#prints <__main__.Person object at 0x10119feb8>
#we need to overload what happend when we call the print method on the Person object
#any methods that Object has are accessible
#dunder = underscore
print([chris])
#the machine representation of our object
#so we can overload one more method

#Bank account example
class BankAccount:

    def __init__(self, balance, acc_name):
        self.balance = balance
        self.acc_name = acc_name

    def __str__(self):
    #overloads the print function
        return "Hello, {}, your balance is ${}.".format(self.acc_name, self.balance)

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            print("Thank you, {}.  Your remaining balance is ${}.".format(self.acc_name, self.balance))
        else:
            print("Sorry {}, you have no money!".format(self.acc_name))

    def deposit(self, amount):
        self.balance += amount
        print("Thank you, {}. Your balance is now ${}.".format(self.acc_name, self.balance))

class BankAccountSpecial(BankAccount):
    #So this new class inherits everything from the one we made.

    def __init__(self, balance, acc_name):
        super().__init__(balance, acc_name)
        #This is telling it to go to the parent and use that stuff

    def withdraw(self, amount):
        if self.balance - amount > 100:
            self.balance -= amount
            print("Thank you, {}.  Your remaining balance is ${}.".format(self.acc_name, self.balance))
        if 100 > self.balance - amount >= 0:
            #This is a PEP8 legit shorthand
            print("Your account would be under the min.")
        else:
            print("Sorry {}, you have insufficient funds!".format(self.acc_name))

#example: a model for a sequel database, you want it to do something extra
#So you need to overwrite the new stuff, then you need to tell it to go back to the original

#So for PEP8, two spaces between functions, unless it's within a class, then one spaces

acc1 = BankAccount(100, 'Katie')

print(acc1)

acc1.withdraw(50)

acc1.deposit(500)

acc1.withdraw(1000)

acc2 = BankAccountSpecial(200, 'Chris')

acc2.withdraw(100)
acc2.withdraw(101)
acc2.deposit(100)
acc2.withdraw(100)
