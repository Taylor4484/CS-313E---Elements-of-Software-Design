"""Given an input word file, select for output exactly those words
   meeting a given filtering criterion.  For example, words of length k,
   words containing a "q", words that are palindromes, etc."""

def filter( word, f ):
    """This returns true or false depending on
    whether or not the word passes the filter.
    f is a functional parameter."""
    return f( word )

def filterFile( inputFileName, outputFileName, f ):
    """Given a file of words, create a new file containing
    those satisfying a filter function f."""
    # Open the input and output files
    inputFile = open(inputFileName, 'r')
    outputFile = open(outputFileName, 'w')

    # We'll count both words input and words output.
    inputcount = 0
    outputcount = 0
    for line in inputFile:
        inputcount += 1
        # Remove extraneous whitespace, if any.
        word = line.strip()
        # Apply the filtering function f. 
        if filter( word, f ):
            outputFile.write( word + "\n" )
            outputcount += 1
            # print( word )
    # Report the words input and output.
    print ("Transferred ", outputcount, " of ", \
               inputcount, " words.")
    # Close both input and output files. 
    inputFile.close()
    outputFile.close()

def isPalindrome( word ):
    """Filter function: check if word is a palindrome."""
    # Only need to check 1/2 the length.
    n = len( word ) // 2
    for i in range( n ):
        if word[i] != word[-(i+1)]:
            return False
    return True

# If you are defining a one line function that you don't expect to 
# call multiple times, you can define it with a "lambda expression."
# I used those for the first three examples below.  You are not 
# expected to understand lambda expressions. 

# Collect words of length 7
f = lambda x: len( x ) == 7
filterFile( "shortwordslist", "wordsOfLength7", f)

# Collect words containing a "q"
f = lambda x: "q" in x
filterFile( "shortwordslist", "wordsQ", f)

# Collect words beginning with 'l'
f = lambda x: x[0] == "l"
filterFile( "shortwordslist", "LWords", f2)

# Collect all palindromes in the wordlist
filterFile( "shortwordslist", "palindromes", isPalindrome)

