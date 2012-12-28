"""This file implements the Wordlist abstract data type.
   A Wordlist is a structure that stores an arbitrary number of
   words.  The main function is to be able to ask whether a word is
   in the wordlist.  Below is the interface:

     Wordlist()                       --> Wordlist object
     addWord( word, f )               --> Wordlist object
     addWordsFromFile( filename, f )  --> Wordlist object
     removeWord( word )               --> Wordlist object
     findWord( word )                 --> Boolean
     len( )                           --> integer

   This is Wordlist Version 1.0, which implements the wordlist
   as a flat unordered list, with linear search. 

"""

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
                print(" Added", count, "words to the wordlist: (%2.5f seconds)" % (time2 - time1))
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


