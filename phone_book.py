running = True
while running:
    try:
        query = int(input('Enter 1 to search phonebook, enter 2 to quit:'))
    except ValueError:
    #this allows your progam to keep running
    #otherwise, Python would kick the user out and stop running
        print('I did not understand that')
        continue
    if query == 1:
        print('thank you')
        running = False
    elif query == 2:
        quit()
    else:
        print('I did not understand that')
