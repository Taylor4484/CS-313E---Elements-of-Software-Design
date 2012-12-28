# File: Assignment1.py
#
# Description: Program opens a user defined file (or default) and runs a
# series of filtering functions to find words that meet a filter function's
# criteria. Any words found are printed to an output file and a summary of the
# program's actions are displayed.
#
# Student's Name: Micheal Taylor McCaslin
#
# Student's UT EID: MTM2275
#
# Course Name: CS 313E 
#
# Date Created: 9/13/12
#
# Date Last Modified: 9/17/12



#set a defult input filename
DEFAULTINPUT = "myWordList.txt"


######################################################################
#                                                                    #
#                           Get Input File                           #
#                                                                    #
######################################################################

def getfile():
    """Asks the user for an input filename. If none is provided (user hit enter)
    use DEFAULTINPUT"""
    
    #Use global defaultinput filename
    global DEFAULTINPUT

    #Tell user the default filename
    print('The default filename is [%s]' % DEFAULTINPUT)

    #Ask the user to accept default or type new filename
    userFileName = input("\tHit 'Enter' to accept, or type new input filename: ")
    
    #Use defaultFile if no input, or use input
    DEFAULTINPUT = userFileName or DEFAULTINPUT


######################################################################
#                                                                    #
#                      Main Filter Function                          #
#                                                                    #
######################################################################

def filterFile( inputFileName, outputFileName, filterfunction ):
    """Main Filter Function accepts two formal parameters and one function parameter
    inputFileName, outputFileName, filterfunction"""
    
    # create a file object associated with the input
    # file specified and open for reading
    myinputFile  = open(inputFileName, 'r')

    # create a file object associated with the output
    # file specified and open for writing
    myoutputFile = open(outputFileName, 'w+')

    #Create list of words from content of myinputFile
    wordList = myinputFile.readlines()

    #Clean the wordlist of extra spaces and line breaks and make everything lowercase
    cleanWordList = [line.strip().rstrip().lower() for line in wordList]
    #Count the number of words read from the inputfile
    listlength = len(cleanWordList)

    # print the number of words read from input (optimized for correct english grammar)
    if listlength == 1:
        print ( "\n", listlength, " word was read from the file:" , inputFileName, "\n", sep='', end='')
    else:
        print ( "\n", listlength, " words were read from the file: ", inputFileName, "\n", sep='', end='')
          
    # create a counter to track how many words are written into output
    counter = 0
    
    # Using Clean World list
    for word in cleanWordList:
        #if the filter function returns words...
        
        if filterfunction( word ):
            
            #increase counter by 1
            counter += 1
            
            # write the word(s) to the output file
            myoutputFile.write( "%s\n" % word )

    #Print the number of words written to output (optimized for correct english grammar)
    if listlength == 1:
        print (counter, "word was filtered and written to:", outputFileName)
    else:
        print (counter, "words were filtered and written to:", outputFileName)
          
    #close open files
    myinputFile.close()
    myoutputFile.close()



    

######################################################################
#                                                                    #
#                         Filter Functions                           #
#                                                                    #
######################################################################   

def hasLength7( word ):
    """Filter function to find words that have a length of 7"""
    return len( word ) == 7

def hasLetterQ( word ):
    """Filter function to find words that contain the letter q"""

    #define a set of letter(s)
    letter = set('q')

    #check for intersection of sets
    if letter & set(word):
        return True

def startsLetterL( word ):
    """Filter function to find words that start with L"""
    if word[0] == 'l':
        return True

def isPalindrome( word ):
    """Filter function to find words that are palindromes"""
    wordbackwards = word[::-1]
    if word == wordbackwards:
        return True




######################################################################
#                                                                    #
#                           Run Automator                            #
#                                                                    #
###################################################################### 


def run():
    """General Run Function container, holds the assignement function calls"""
    global DEFAULTINPUT
    inputFileName = DEFAULTINPUT
    filterFile( inputFileName, "wordsofLength7.txt", hasLength7 )
    filterFile( inputFileName, "wordsQ.txt", hasLetterQ )
    filterFile( inputFileName, "LWords.txt", startsLetterL )
    filterFile( inputFileName, "palindromes.txt", isPalindrome )




getfile()   
run()

