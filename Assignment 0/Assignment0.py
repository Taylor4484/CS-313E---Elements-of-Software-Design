# File: Assignment0.py
#
# Description: Caesar Cipher Encoder. Takes a user inputted string,
# shows it in uppercase, lowercase, counts the letter occurrence,
# prints using the caesar cipher (1 letter) and then waits for
# another input from the user. The user can type "exit" to end the
# the program, where a thank you message will be shown.
#
# Student's Name: Micheal Taylor McCaslin
#
# Student's UT EID: MTM2275
#
# Course Name: CS 313E 
#
# Date Created: 9/6/12
#
# Date Last Modified: 9/10/12



######################################################################
#                                                                    #
#                           Global Variables                         #
#                                                                    #
#                       Define global variables                      #
######################################################################

#the keys that you want to count and replace with a caesar cipher
#can be any char
KEY = ["a","b","c","d","e","f","g","h","i","j","k","l",  
    "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#sets an initial state of the program, can be any string
VALUE = " "

#A default shift of 1 letter (a=b, b=c, etc), can be any int
SHIFT = 1


######################################################################
#                                                                    #
#                           Key Encoder                              #
#                                                                    #
# Creates a dic of keys and their shift value, returns encoded input #
######################################################################


# define the encoder program with a default shift of 1 letter (a=b, b=c, etc)
def coder():  
    """coder() uses the global variable SHIFT to determine how many
    letters to shift an encoded value. The global default of 1 letter
    results in a=b, b=c, etc"""

    #use the global variable SHIFT
    global SHIFT
    
    #Swap key values
    dic = {}  
    for i in range(0,len(KEY)):  
        dic[KEY[i]] = KEY[(i+SHIFT)%len(KEY)]  
  
    #Change input to lower case and encode with swapped key values
    encoder=""
    for x in VALUE.lower():  
        if x in dic:  
            x = dic[x]  
        encoder += x  
  
    return encoder


######################################################################
#                                                                    #
#                          Letter Counter                            #
#                                                                    #
#  Counts the chars in a user's input and visually represents them   #
######################################################################

def counter():
    """counter() counts the occurrences of characters in key values
     and prints a readable summary"""
    
    #import counter function
    from collections import Counter


    #define what to count
    counter = Counter(VALUE.lower())

    #iterate over key list values and count for each value
    for char in KEY:
        print ("\t",char,":", counter[char])
    


######################################################################
#                                                                    #
#                           Caesar Cipher                            #
#                                                                    #
#  Asks for input, prints it, runs counter, runs loop until 'exit'   #
######################################################################

def caesar():
    """caesar() asks a user for a string and then encodes it using
    a caesar cipher based on the global variables"""

    #use the global variable VALUE 
    global VALUE
    
    #welcome user and give instructions
    print ('Welcome to the Caesar Cipher!')
    print ('\n\tThis program will encode values as they are entered.\n\t- To quit, type the word "exit"')
      
    #loop the caesar cipher   
    while VALUE:

        #get user input
        VALUE = input("\nPlease enter a string: ")

        #if "exit" is typed, display thank you message and exit program loop, allow defined variation
        if VALUE in ('exit', 'EXIT', 'Exit'):
            print ("\nThank you for using the Caesar Cipher!")
            break
        
        #display what was typed, then in upper case and then in lower case
        print ("\n\tYou typed:", VALUE)
        print ("\n\t\tIn uppercase:", VALUE.upper())
        print ("\t\tIn lowercase:", VALUE.lower())

        #display the letter counter
        print ("\n\tThe input contains the following characters:\n")
        counter()

        #display the caesar cipher
        print ("\n\tUsing the Caesar Cipher:",coder())

        #display reminder about quitting
        print ('\n\n** Remember: to quit, type the word "exit" **')


caesar()
