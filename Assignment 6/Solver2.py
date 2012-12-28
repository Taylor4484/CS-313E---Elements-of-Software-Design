#  Files: Permutations.py, Wordlist.py, Solver.py
#
# Description: An interactive jumble solver. Imports a dictionary file and checks permutations of
# inputed words against the dictionary and proivdes stats
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


#import needed modules
import time
from collections import Counter

######################################################################
#                                                                    #
#                           Permutations                             #
#                                                                    #
######################################################################

"""This module contains functions to generate all unique permutations
   of a string, and to count permutations."""

import math

def countOccurrences( word ):
    # create a list of 26 0s to count occurrences of each
    # letter.
    word = word.lower()
    occurs = [0]*26
    for ch in word:
        i = ord(ch) - ord('a')
        occurs[i] += 1
    return occurs

def howManyPerms( word ):
    """Return the number of permutations and unique
       permutations of a string."""
    word = word.lower()
    n = len( word )
    # count the occurrences of each letter in word.
    occurs = countOccurrences( word )
    # For any letter that recurs, the number of unique
    # permutations is the totalPerms divided by the 
    # factorial of that count. 
    divisor = 1
    for i in range(26):
        if occurs[i] > 1:
            divisor *= math.factorial( occurs[i] )
    totalPerms = math.factorial( n )
    uniquePerms = totalPerms / divisor
    return ( totalPerms, uniquePerms )

# Fixed this so that it doesn't return duplicates. 

def allPermsAux( word, permsSeen ):
    """This is an auxiliary function that generates all
    unique permutations of the input string not already in
    the list permsSeen."""
    if len( word ) <=1:
        yield word
    else:
        for perm in allPermsAux( word[1:], permsSeen ):
            for i in range( len( perm )+1 ):
                newperm = perm[:i] + word[0] + perm[i:]
                if not newperm in permsSeen:
                    permsSeen.append( newperm )
                    yield newperm


def allPerms( word ):
    """This function generates all unique permutations of the 
    input string."""
    return allPermsAux( word, [] )



######################################################################
#                                                                    #
#                           Wordlist ADT                             #
#                                                                    #
######################################################################

class Wordlist:
    """Define a Wordlist ADT"""

    def __init__( self ):
        """create an empty Wordlist."""
        self._wordlist = []
        
    def __len__( self ):
        """Return length of the queue"""
        return len( self._wordlist )

    def isEmpty( self ):
        """Boolean of if the wordlist is empty or not"""
        return self._wordlist == []

    def addWord( self, word, f ):
        """add a word to the Wordlist, if it satisfies filter function f."""
        #check that the word meets the criteria len of f 
        if len(word) == (f):
            self._wordlist.append( word )

    def addWordsFromFile( self, filename, f ):
        """given an external file containing words, add to the Wordlist any
        that satisfy f. Assume that the file contains one word per line,
        and that the words do not repeat."""

        self._inputFile = open( filename, 'r' )

        for line in self._inputFile:
            # Remove extraneous whitespace, if any.
            word = line.strip()
            # Apply the filtering function f. 
            self.addWord( word, f )

        # Close input file. 
        self._inputFile.close()


    def removeWord( self, word ):
        """remove the word from the Wordlist."""
        #check if the word is in the list
        if word in self._wordlist:
            #remove the word
            self._wordlist.remove( word )
        else:
            #word not in list, print message
            print ( "%s is not in wordlist" %word )

    def findWord( self, word ):
        """ a pair ( Boolean, integer ) indicating whether or not the word is
        in the wordlist and how many comparison you performed to determine."""
        counter = 0

        #for each word checked, increase counter and check if it's the word
        for item in self._wordlist:
            counter += 1
            #if it's the word, return true and how many words checked
            if word == item:
                return ( True , counter )
            else:
                #word not it, keep checking
                continue
        #word not found, return false and how many words checked
        return ( False, counter )

    def __str__( self ):
        """print the wordlist"""
        #used for testing
        return str(self._wordlist)

    def __iter__ ( self ):
        """allow iterating over the wordlist object"""
        return iter(self._wordlist)

        
        



######################################################################
#                                                                    #
#                        Create Wordlist                             #
#                                                                    #
######################################################################


#create wordlist, import words of len 5 or 6
wl = Wordlist()

#set a filename
filename = "scrambledwordslist.txt"

#start timer
start = time.time()

#import words from filename
wl.addWordsFromFile( filename , 5 )
wl.addWordsFromFile( filename , 6 )

#stop timer
end = time.time()

print ("Using words from %s" %filename)
print ("The Wordlist contains ", str(len(wl)))
print ("Building the Wordlist took %2.3f seconds" % (end - start))


######################################################################
#                                                                    #
#                           Jumble Finder                            #
#                                                                    #
######################################################################

#Keep program running until exit
while True:

    #user inputs word (or type 'exit')           
    word = input("\nEnter a scrambled word (or EXIT): ")

    #check for actual input, if none, re-ask
    if word == "":
        continue

    #check lower case name for the word 'exit'
    if word.lower() == "exit":
        print ("Thanks for playing! Goodbye.")
        break


######################
# Counter Method
######################

    start = time.time()
    countercounter = 0
    
    #for each word in wordlist
    for item in wl:

        countercounter += 1

        #Did I find it?
        found = False

        #set counters
        inputvalue = Counter(word)
        testword = Counter(item)
        
        #stop if counters match for inputed word and word in wordlist
        if inputvalue == testword:
            #found it
            found = True
            foundword = item
            break
        
        #otherwise, keep looking
        else:
            continue

    #stop clock
    end = time.time()

    countertime = (end - start)

    if found == False:
        print("\nWord Not Found")
        print ("Solving this jumble took %2.3f seconds using counter." % countertime)
        print ("Made %s comparisons.\n" % countercounter)

    elif found == True:
        print ("\nWord Found: %s" % foundword)
        print ("Solving this jumble took %2.3f seconds using counter." % countertime)
        print ("Made %s comparisons.\n" % countercounter)

        
######################
# Permutation Method
######################

    #start timer
    start = time.time()
    
    #check for permutations
    perms = howManyPerms( word )

    #process howManyPerms returned value
    totalPerms = perms[0]
    uniquePerms = perms[1]
    
    print ("Found ", totalPerms, " permutations and ", uniquePerms, " unique permutations.")

    #get all permutations of word
    tries = allPerms( word )

    #permutations checked counter
    permcounter = 0

    #comparison counts (sums comparisons of all tried permutations)
    compcounter = 0

    for perm in tries:
        permcounter += 1
               
        #serch wordlist for perm in this try
        found = wl.findWord( perm )

        #if found stop looking
        if found[0] == True:
        
            #add comparisons to compcounter
            compcounter += found[1]
            print ("Found word: ", perm)
            break
        
        #try new permutation
        else:
            
            #add comparisons to compcounter
            compcounter += found[1]
            continue
           
    
    #stop timer
    end = time.time()

    permtime = (end - start)

    if found[0] == True:
        print ("Solving this jumble took %2.3f seconds using permutations." % permtime)

    if found[0] == False:
        print ("I tried for %2.3f seconds, but found no solution using permutations." % permtime)
        
    print ("Checked %s permutations." % permcounter)
    print ("Made %s comparisons." % compcounter)



######################################################################
#                                                                    #
#                         Efficiency Data                            #
#                                                                    #
######################################################################


    #calculate some efficiency data
    timesaved = permtime - countertime
    savedcomparisons = (compcounter-countercounter)
    efficiency = round((compcounter/countercounter)*100)

    print ("\n\tUsing counter saved %2.3f  seconds." % timesaved)
    print ("\tUsing counter saved %s comparisons." % savedcomparisons)
    print ("\tUsing counter was %s percent more efficient than using permutations." % efficiency)
