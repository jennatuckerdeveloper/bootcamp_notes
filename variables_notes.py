#variables should be nouns, ex. found_name, full_name
print(1 + 1)
print("string" * 10) #This will print the string 10 times.

trip_miles = int(input("How many miles is this trip? "))
mpg = int(input("How many miles per gallon does your car get? "))
gas_cost = float(input("How much does gas cost per gallon? "))

trip_cost = (trip_miles / mpg) * gas_cost

print("Your trip will cost $" + str(trip_cost))
