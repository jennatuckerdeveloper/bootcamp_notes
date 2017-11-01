#default values in function perameters
#i.e. what to call if nothing specific is entered

#if you give a perameter but hardcode a defaul answer
#into the function, then it will still replace it if
#you enter something new when you call the function

#your non-default argument needs to come before your
#default argument

from random import randint

def dice_roll(num_dice, num_side=6):
    num_dice = int(num_dice)
    num_side = int(num_side)
    while num_dice > 0:
        print("Roll: ", randint(1, num_side))
        num_dice = num_dice - 1

num_dice = input("How many dice do you want to roll? ")
num_side = input("How many sides do you want each dice to have? ")
print(dice_roll(num_dice, num_side))

num_dice = input("How many dice do you want to roll? ")
print(dice_roll(num_dice))

#you can list your parameters out of order if you label them:
#for example: dice_roll(num_side=5, num_dice=10)
