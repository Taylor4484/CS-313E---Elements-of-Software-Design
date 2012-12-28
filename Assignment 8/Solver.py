#  Files: Permutations.py, Wordlist.py, Solver.py, README
#
#  Description: This is a program to solve the Jumble in the newspaper or online.
#
#  Student's Name: Micheal Taylor McCaslin
#
#  Student's UT EID: MTM2275
#
#  Course Name: CS 313E 
#
#  Date Created: 11/12/2012
#
#  Date Last Modified: 11/12/2012



######################################################################
#                                                                    #
#                               Solver                               #
#                                                                    #
######################################################################


import time
import Wordlist
import Permutations
import sys
    

inputFileName = "scrambledwordslist.txt"

def main():
    start = time.time()
    
    #check's for appropriate number of command line arguments and executes depending on them
    if len( sys.argv ) < 2:
        print("Please supply a command line argument: flat or sort.") 
        sys.exit()   
    elif sys.argv[1] == "flat":
        wordlist = Wordlist.Wordlist()
        print("Using flat unsorted wordlist.")
    elif sys.argv[1] == "sort":
        wordlist = Wordlist.SortedWordList()
        print("Using sorted wordlist.")

    # We only add words to the Wordlist if they have 5 or 6 letters.
    wordlist.addWordsFromFile( inputFileName, lambda x: len(x) in [5, 6] )
    print( "\nThe Wordlist contains ", len( wordlist ), " words.")
    end = time.time()
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

        # Create a list of all permutations of the input
        # string. 

        # print out how many unique perms there are.
        permsCount, uniquePermsCount = Permutations.howManyPerms( word )
        print("Found ", permsCount, "permutations; ", uniquePermsCount, "unique permutations")

        # We're going to check how many permutations we generated, and
        # how many comparisons were made against words in the wordlist.
        permutationsChecked = 0
        comparisonsMade = 0

        # Iterate through the permutations until you find one that is 
        # in the wordlist, or 5ail if there are no hits. 
        found = False
        for p in Permutations.allPerms( word ):
            permutationsChecked += 1
            permInList, comparisons = wordlist.findWord( p )
            comparisonsMade += comparisons
            if permInList:
                print ("Found word: " + p)
                found = True
                # With the break, stops after the first hit.  Without it, 
                # this tries all of the permutations.
                break
        if not found:
            print("Sorry.  I can't solve this jumble!  Try again.")
        end = time.time()

        # Print out the stats on this attempt.
        print("Solving this jumble took %2.5f seconds" % (end - start))
        print("Checked ", permutationsChecked, " permutations.")
        print("Made ", comparisonsMade, " comparisons.")
    
main()
