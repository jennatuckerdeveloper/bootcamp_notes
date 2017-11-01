#this will do full dollars as four quarters
change = float(input('What is the total amount? '))
#takes the amount of money and ensures that it was a decimal point
def change_retrun(ch):
    total = int(ch * 100)
    #converts the sum into cents, so $1 is 100 cents
    final = {}
    #creates a dictionary
    while total > 0:
        #gives this an ending when the sum is fulfilled
        if total - 25 >= 0:
            #starts with checking for 25 cents at a time
            if 'quarters' in final:
                final['quarters'] += 1
            #if there is already 1 quarter, this adds one and changes the value
            else:
                final['quarters'] = 1
            #this adds a key of quarters and a value of 1 if any quarters
            total -= 25
        elif total - 10 >= 0:
            if 'dimes' in final:
                final['dimes'] += 1
            else:
                final['dimes'] = 1
            total -= 10
        elif total - 5 >= 0:
            if 'nickles' in final:
                final['nickles'] += 1
            else:
                final['nickles'] = 1
            total -= 5
        elif total - 1 >= 0:
            if 'pennies' in final:
                final['pennies'] += 1
            else:
                final['pennies'] = 1
            total -= 1
    text_return = 'Your change is: '
    for k, v in final.items():
        text_return += '{}: {}, '.format(k, v)
    print(text_return[:-2] + '.')

change_retrun(change)
