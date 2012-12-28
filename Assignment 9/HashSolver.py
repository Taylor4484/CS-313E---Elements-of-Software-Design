#  Files: Wordlist.py, HashSolver.py, README
#
#  Description: This is a program to solve the Jumble in the newspaper or online.
#
#  Student's Name: Micheal Taylor McCaslin
#
#  Student's UT EID: MTM2275
#
#  Course Name: CS 313E 
#
#  Date Created: 11/28/2012
#
#  Date Last Modified: 11/28/2012


######################################################################
#                                                                    #
#                               Solver                               #
#                                                                    #
######################################################################


import time
import Wordlist
    

inputFileName = "scrambledwordslist.txt"

def main():
    start = time.time()
    print("Creating the Wordlist\n")
    wordlist = Wordlist.HashedWordList()
    # We only add words to the Wordlist if they have 5 or 6 letters.
    wordlist.addWordsFromFile( inputFileName, lambda x: len(x) in [5, 6] )
    end = time.time()
    wordlist.loadfactor()
    print("Building the Wordlist took %2.3f seconds" % (end - start))
    
    # Execute this loop until the user decides to exit. 
    while True:
        word = input ("\nEnter a scrambled word (or EXIT):  ")
        start = time.time()
        word = word.strip().lower()
        # See if the word contains bad characters.
        if not word.isalpha():
            print( "Word contains illegal characters. Try again" )
            continue
        # Should we terminate 
        elif (word == "exit"):
            print( "Thanks for playing!  Goodbye." )
            break
        # There's no need searching the Wordlist if the word isn't 
        # a plausible length. 
        elif not len( word ) in [5, 6]:
            print( "Word must have 5 or 6 letters.  Try again" )
            continue

        #Create variables for returned values of findPerm
        Found, Jumble, comparisonsMade = wordlist.findPerm(word)

        if Found:
            print ("Found word: " + Jumble)

        if not Found:
            print("Sorry.  I can't solve this jumble!  Try again.")
            
        end = time.time()

        # Print out the stats on this attempt.
        print("Solving this jumble took %2.5f seconds" % (end - start))
        print("Made ", comparisonsMade, " comparisons.")
    
main()
