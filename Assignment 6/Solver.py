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
# Date Created: 10/28/12
#
# Date Last Modified: 10/28/12


#import needed modules
from Wordlist import *
from Permutations import *
import time

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

    if found[0] == True:
        print ("Solving this jumble took %2.3f seconds." % (end - start))

    if found[0] == False:
        print ("I tried for %2.3f seconds, but found no solution" % (end - start))
        
    print ("Checked %s permutations." % permcounter)
    print ("Made %s comparisons." % compcounter)
