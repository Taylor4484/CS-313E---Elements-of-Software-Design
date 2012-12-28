#  Files: Permutations.py, Wordlist.py, Solver.py
#
# Description: Wordlist ADT. Creates a list of words that has mutators
# and accessors
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

        
        
