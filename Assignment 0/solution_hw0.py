"""This is the solution to assignment 0. The point is to write a
simple Python program that does some simple string manipulations:

1. Accept string inputs from the user
2. Print the input, print again in upper and lower case. 
3. Assuming a lowercase version, display the count of occurences of 
   each letter.
4. Finally, display the Caesar Cipher of the input, shifting each
   character by one place. 
5. Exit when an empty string is entered. 
"""

while True:
    # Prompt for user input.
    inp = input( "\nPlease enter a string: " )
    # Exit if the input string is empty.
    if ( inp == "" ): break
    
    # Print the input, an uppercase version, and a lowercase version.
    print ( "User's input: ", inp )
    print ( "In uppercase: ", inp.upper() )
    print ( "In lowercase: ", inp.lower() )

    # Count occurences of the letters a-z
    counts = [0] * 26
    for c in inp.lower():
        # Ignore non-letters.
        if c.isalpha():
            index = ord(c) - ord("a")
            counts[index] += 1

    # Print the letter counts.
    print ( "The input contains the following characters:")
    for i in range(26):
        print ( "   " + chr (i + ord('a')) + ":", counts[i])

    # Apply Caesar cipher with a shift of one position. 
    caesar = ""
    for c in inp.lower():
        # z must be treated specially.
        if ( c == "z" ):
            caesar += "a"
        elif c.isalpha():
            caesar += (chr (ord(c) + 1))
    print ( "Using the Caesar cipher:", end=" ")
    print (caesar)

        
