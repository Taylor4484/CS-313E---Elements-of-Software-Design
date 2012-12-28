#  Files: Wordlist.py, HashSolver.py, README
#
#  Description: Wordlist and Sorted Wordlist ADT
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


import time

######################################################################
#                                                                    #
#                       Flat Unordered Wordlist                      #
#                                                                    #
######################################################################

class Wordlist:
    """A Wordlist stores an arbitrary number of words.  The main
       function is to be able to ask whether or not a word is 
       in the Wordlist.  We can also add and remove words."""

    def __init__(self):
        """Create an empty Wordlist."""
        self._words = []
        self._wordCount = 0

    def __len__(self):
        return self._wordCount

    def isEmpty( self ):
        return not self._words

    def addWord(self, word, f):
        """Add a single word to the Wordlist."""
        if f( word ):
            self._words.append( word )
            self._wordCount += 1

    def addWordsFromFile( self, filename, f ):
        """Given an external file containing words, add
           each to the Wordlist.  Assume that the file
           contains one word per line, and that the words
           do not repeat."""
        inputFile = open( filename, 'r' )
        count = 0
        for line in inputFile:
            time1 = time.time()
            word = line.strip()
            self.addWord( word, f )
            # Because the wordlist building is slow, added
            # this to give some indication of progress. 
            count += 1
            if ( count % 1000 == 0 ):
                time2 = time.time()
                #altered to better reflect what was happening (processing words)
                print(" Processed", count, "words from the input file in %2.6f seconds" % (time2 - time1))
        inputFile.close()

    def removeWord( self, word ):
        """This removes the first occurrence of the word.
           Assumes only one occurrence."""
        if self.findWord( word ):
            self._words.remove( word )
            self._wordCount -+ 1
        else:
            print("Word", word, "not found in wordlist.")

    def findWord( self, word ):
        """Find a word in the Wordlist via linear search.  This 
           could use the Python in operator, but that would be 
           difficult to meter.  Returns a pair containing the 
           boolean result and the number of comparisons made."""
        for i in range( len( self._words ) ):
            if self._words[i] == word:
                return ( True, i+1 )
        return ( False, len( self._words ) )

    def __str__( self ):
        """print the wordlist"""
        #used for testing
        return str(self._words)


######################################################################
#                                                                    #
#                            Sorted Wordlist                         #
#                                                                    #
######################################################################

class SortedWordList(Wordlist):
    """A Sorted Wordlist stores an arbitrary number of words.  The main
   function is to be able to ask whether or not a word is 
   in the Wordlist.  We can also add and remove words."""

    def __init__(self):
        """Initialize from Wordlist"""
        #initialize Wordlist
        Wordlist.__init__(self)


    def insertionSort(self, lst, word):
        """Given a list and a word, insert the word into the appropriate place
        in the list via insertionSort"""
        insert = False

        #Base Case
        if len(lst) == 0:
            lst.append(word)
        #otherwise, iterate over lst, insert word in appropriate place
        else:
            for i in range(0,(len(lst))):
                index = i
                if word < lst[i]:
                    lst.insert(i, word)
                    insert = True
                    break
                else:
                    continue
        #if through whole list no place found, append at the end.
        if insert == False:
            lst.append(word)
                
        return lst

        
    def binarySearch(self, lst, x, lo, hi ):
        """This implements a binary search for x on a
        list lst, between indices lo and hi. True
        is returned if x is found, else False is returned."""
        comparisons = 0
        while lo < hi:
            comparisons += 1
            mid = (lo + hi)//2
            midval = lst[mid]
            if midval < x:
                lo = mid+1
            elif midval > x: 
                hi = mid
            else:
                return (True, comparisons)
        return (False, comparisons)


    def addWord(self, word, f):
        """Add a single word to the Wordlist."""
        if f( word ):
            self.insertionSort(self._words, word)
            self._wordCount += 1

    def findWord( self, word ):
        """Find a word in the Wordlist via linear search.  This 
           could use the Python in operator, but that would be 
           difficult to meter.  Returns a pair containing the 
           boolean result and the number of comparisons made."""
        return self.binarySearch( self._words, word, 0, len( self._words ))

    def __str__( self ):
        """print the wordlist"""
        #used for testing
        return str(self._words)

######################################################################
#                                                                    #
#                             Hash Table                             #
#                                                                    #
######################################################################


class HashedWordList(Wordlist):
    """A Sorted Wordlist stores an arbitrary number of words.  The main
   function is to be able to ask whether or not a word is 
   in the Wordlist.  We can also add and remove words."""

    
    def __init__(self):
        """Initialize HashTable from Wordlist"""
        
        #initialize Wordlist
        Wordlist.__init__(self)
        
        #set tableSize
        self._tableSize = 10007
        
        #create hashtable
        self._hashTable = []
        #make it a list of lists (fixes bug where all lists of
        #lists are same object)
        for k in range(self._tableSize):
            self._hashTable.append([])
            
        #prime list
        self._PRIMES2 = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, \
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, \
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113, \
        127, 131, 137, 139, 149, 151, 157, 163, 167, 173 ]

    def addword(self, word, f):
        """Add a single word to the Hashed Wordlist."""
        if f( word ):
            self._wordCount += 1
            h = self.computeHash3( word, self._tableSize )
            self._hashTable[h].append(word)
  
    
       
    def addWordsFromFile(self, filename, f):
        """Given an external file containing words, add
           each to the Hashed Wordlist."""
        inputFile = open( filename, 'r' )
        for line in inputFile:
            word = line.strip()
            self.addword( word, f )
        inputFile.close()


    def loadfactor (self):
        """calculate load factor statistics for the hashtable"""
        countZeros = 0
        #variables needed to calculate average without using math library
        sumation = 0
        count = 0
        for i in range( self._tableSize ):
            #what is the length of the list
            size = len(self._hashTable[i])
            #if greater than zero, add len to sumation and increase count
            if size > 0: sumation += size; count += 1
            #if equal to zero, increase countZero
            if size == 0: countZeros += 1
        else:
            print( "The Wordlist contains %s words." % self._wordCount )
            print( "There are %s empty buckets" % countZeros )
            print( "Non-empty buckets have an average length of %2.3f words" \
            % (sumation/count) )
        
    def findPerm( self, word ):
        """Find a word in the Wordlist via linear search.  This 
           could use the Python in operator, but that would be 
           difficult to meter.  Returns a pair containing the 
           boolean result and the number of comparisons made."""
        h = self.computeHash3( word, self._tableSize )
        counter = 0
        for i in self._hashTable[h]:
            counter += 1
            if sorted(i) == sorted(word):
                return (True, i, counter)
        else:   
            return (False, None , counter)
        
    def computeHash3 (self, word, tableSize ):
        """Compxute the index i of the character in the range [a..z].
        Then multiply by the ith prime. This hash will have the attribute
        that it is indifferent to permuations."""
        hash = 1
        for ch in word:
            i = ord(ch) - ord('a')
            hash *= self._PRIMES2[i]
        return hash % self._tableSize
