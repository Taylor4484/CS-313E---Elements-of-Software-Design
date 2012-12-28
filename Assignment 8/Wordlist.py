#  Files: Permutations.py, Wordlist.py, Solver.py, README
#
#  Description: Wordlist and Sorted Wordlist ADT
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
