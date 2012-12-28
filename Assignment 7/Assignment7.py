#  Files: Assignment7.py, any classes you use
#
# Description: Program to sort a list of random integers using Radix sort.
#
# Student's Name: Micheal Taylor McCaslin
#
# Student's UT EID: MTM2275
#
# Course Name: CS 313E 
#
# Date Created: 10/29/12
#
# Date Last Modified: 10/29/12


import random
import math

def printlist(lst, num):
    #counter (items per line)    
    counter = 0
    #value (i) index count
    value = 1

    #print the opening list bracket
    print("[   ", end="")
    
    for i in lst:
        counter += 1
        
        #print each item,aligned to 3 decmial places with no line end
        print("%3d" %i, end=" ")

        # if i is the last in the lst, print the closing bracket
        if value == len(lst):
                print("   ]\n")

        #if counter = num, create a new line and continue
        elif (counter == num):
            #reset counter
            counter = 0
            print("\n    ", end="")
        #increase the current value index count      
        value += 1


            
def radixSort(lst, passes):
    #sets the digit comparison number for string value
    charnumber = -1
    
    #iterate over the number of passes
    for i in range(passes):
    
        #create a list of ten lists
        passlist = [[],[],[],[],[],[],[],[],[],[]]
        
        for x in lst:
            if x == []:
                continue
            number_string = str(x).zfill(passes)
            #get digit that matches the pass number (ie first digit for last pass)
            digitvalue = int(number_string[charnumber])
            passlist[digitvalue].append(x)
        #create a new 
        lst = []

        for i in range(10):
            for value in passlist[i]:
                lst.append(value)
                       
    #reduce the char number for each pass
        charnumber -= 1
    #pass the lst back
    return lst

 
# This will generate a list of 200 numbers randomly generated
# in the range 0..999.
input = [ random.randint(0, 999) for i in range(200) ]

# You have to write the printList function to print the list, k = 20
# numbers per line.
print ("\nThe input list is: ")
printlist(input, 20)

# This is the function that actually sorts the list, using k = 3
# rounds 
output = radixSort(input, 3)

# Print the sorted result.
print ("\nThe sorted list is: ")
printlist(output, 20)



        
        
        
