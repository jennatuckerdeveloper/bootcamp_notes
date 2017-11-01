time = input("Enter the current hour with AM or PM to see what real time it is: "
)
time = time.upper()

def this_mealtime(time):
    if time == "7AM" or time == "8AM" or time == "9AM":
        print("Breakfast")
    elif time == "12PM" or time == "1PM" or time == "2PM":
        print("Lunch")
    elif time == "7PM" or time == "8PM" or time == "9PM":
        print ("Dinner")
    else:
        print ("Hammer")

this_mealtime(time)

#make a version that converts a time and/or rounds the time
