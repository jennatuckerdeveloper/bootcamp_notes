#terminal i/o, input/output
#everytime we've run our programs, it resets the data
#so when we do inputs, then we leave, that's that.  It's gone.
#if we want to read information and store information,
#we use file i/o

#opening and closing things
#files are opened to read their contents
#file open takes a file name and opens a file object
#then you close it
#it doesn't go back to the top
#if you don't close it, this will stay in memory
#once you close it, it's taken out of memory
#so we want to ensure that when we open files, we close them
#use the reserved word with
#with open as phone_book_file
#after code block, the computer will automatically close files

#with is building in the close before you even get going
#safer way to read a file

#open takes in two arguments
#first is the name of the file relative to where you are now
#right now, I am in the same folder as this text file
#otherwise, I would have a filepath relative to where I am
#the second argument is a flag that says what we're doing
#r = read, w = write and read

with open('test_text.txt', "r") as text:
    print(text.readlines())
    #if we make this readlines(0), we get the first line.
    #it's indexable, so we could do a slice

with open('test_text.txt', "r") as text:
    for line in text.readlines():
        print(line)

#copy a file to a new file
with open('test_text.txt', 'r') as text:
    with open('this_thing.txt', 'w') as new_txt:
        for line in text.readlines():
            new_txt.write(line)
