"""This is a program to solve the Jumble in the newspaper or online.
   It first builds a Wordlist structure from the words in the designated
   sourcefile.  Then, the program enters a loop in which it carries
   out the following steps:

   1. prompt the user for a jumbled word;
   2. generate permutations of the jumble;
   3. test each permutation to see if it's in the wordlist;
   4. if so, print the solution and continue;
   5. if not, print a failure message and continue.

   For each stap of the process, keep statistics on time and space
   usage.  

   """

######################################################################
#                                                                    #
#                               Solver                               #
#                                                                    #
######################################################################


import time
import Wordlist1
import Permutations

inputFileName = "scrambledwordslist"

def main():
    start = time.time()

    wordlist = Wordlist1.Wordlist()
    print("Using flat unsorted wordlist.")

    # We only add words to the Wordlist if they have 5 or 6 letters.
    wordlist.addWordsFromFile( inputFileName, lambda x: len(x) in [5, 6] )
    print( "The Wordlist contains ", len( wordlist ), " words.")
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
        # in the wordlist, or fail if there are no hits. 
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
