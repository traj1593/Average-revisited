'''
Program: Average Revisited
Filename: averageRevisited-tRaj-00.py
Author: Tushar Raj
Description: calculate the average of a sequence of numbers when no value is entered
Revisions: No revisions made
'''
#There is no import statement
#There are no literal constraint
#There are no class defined

def inputdata(number): #checks the user input is correct
    '''
    This function accepts the input from the user and checks if the value contains any special character,alphabets.It even checks that the value is not negative for the number of sequence
    Input: user input from the console which is string type
    output: returns converted strings into float/int data type
    '''
    count = 1
    special = "!@#$%^&*()+?_=,<>/"
    alphabet = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm"
    while(count):
        if(any( i in alphabet for i in number)): #checks if the value entered in number variable is having any character or not
            print("****Entered value can not have characters****\n") #prints the error message
            progress = input("Please enter if you want to continue with computation of Simple Average(y/n): ") #ask users if he wants to continue with program
            if( progress == 'y' or progress == 'Y' ):#checks the response of the user if its yes, asks to enter the diameter again
                number = input("\nEnter a number: ")
            if( progress == 'n' or progress == 'N' ):#exits the program if response in no
                exit()
            continue
        elif (any( i in special for i in number)): #picks up each character from the number variable and then checks in special variable if it is present, if present run this elif
            print("****Input cant have special character. Please Enter the valid entry****\n")
            progress = input("Please enter if you want to continue with computation of Simple Average(y/n): ")
            if( progress == 'y' or progress == 'Y' ):
                number = input("\nEnter a number: ")
            if( progress == 'n' or progress == 'N' ):
                exit()
            continue
        else:
            return number



### Step 1: Announce, prompt and get Response
print("Average Revisited:")
print("Program to compute the average of the numbers provided.\n")

print("Enter each number followed by <enter>.")
print("When you are done, just hit <enter> in response to the prompt.\n")

#Prompt user to get the number for average
sequence_value,addition = 0,0
while user_input := input("Enter a number: "): #walrus operator It allows to assign a value to a variable while also returning the value 
        number = inputdata(user_input) #checking if the user input is valid or not
        addition += float(number) #adding all the user input
        sequence_value+=1 #keeping count of value entered

###Step 2: Calculate the simple average and print the result
try:
    simple_average = addition/sequence_value
    print("\nYou entered {0} numbers.".format(sequence_value))
    print("The average is {0}.".format(simple_average))
except ZeroDivisionError:
    print("\nYou entered {0} numbers.".format(sequence_value))
    print("The average is 0.")

print("\n\n****Average Revisited program ended****")
