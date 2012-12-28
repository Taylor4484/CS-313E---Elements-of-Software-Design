#  Files: Permutations.py, Wordlist.py, Solver.py, README
#
#  Description: Analysis of the difference between use of sorted, 
#		flat and hashed wordlist using test cases of 5 words 
#		of length 5 and 6.
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

Creating the Wordlist
The time taken to create the wordlist when using the flat wordlist was .114 seconds.
The time taken to create the wordlist when using the sorted wordlist was 13.592 seconds.
The time taken to create the wordlist when using the hashed wordlist was .173 seconds.

The drastic difference between these times is that the flat wordlist simply appends words
to the end of the list as it meets the filter criteria, whereas the sorted wordlist
takes each word and inserts it properly into the alphabetically sorted wordlist and the hashed wordlist hashes each filtered word and places it into the hash table.

Taking the time to sort the wordlist up front, drastically cuts the number of comparisons by
allowing the program to use binary search to find items from a sorted list. Hashing the wordlist allows
an easy accessor for words as words with the same permutations hash to the same location without having
to check for permutations.

What Stated The Same
In both flat and sorted wordlist the number of permutations is equal for both the sorted and flat 
wordlist, this is expected. Each implementation finds the exact same jumbled word, again expected. 
The hash version doesn't even have to use permutations because all permutations of words will hash
to the same location. So you don't waste effort calculating them, and then you don't have to compare them.
The huge difference comes with the number of comparisons made when solving a jumble. 

What Was Different
The sorted wordlist never got above 1,000 comparisons for words length 5, or 6,000 for
words of length 6. Whereas the flatword list was consistently no LESS than 500,000
comparisons for words of length 5, or 2,000,000 comparisons of length 6. The sorted
wordlist was approximately 500 times more efficient for words of length 5, and 
approximately 333 times more efficient for words of length 6. Using binary search
the sorted wordlist is able to drastically cut down the number of items it searches by
cutting the list it searches in half each pass, where as the flat wordlist simply searches
the entire list each pass. When you are making upwards of 1,000 or 6,000 comparisons, this
makes a huge difference.
The hashed wordlist never got above 10 comparisons, because once a word is hashed all that has to be 
done is search the hashed location's list for words that have the same letters. This is hugely efficient
both in time and effort. You are doing a fraction of the work searching because each word has a
calculable hashed location.


######################################################################
#                                                                    #
#                               Test Words                           #
#                                                                    #
######################################################################

Words of Length 5
fhist - shift
catex - exact
dentr - trend
tioid - idiot
shsal - slash


Words of Length 6
leyngt - gently
trogof - forgot
gewhit - weight
yalelv - valley
ounteg - tongue



######################################################################
#                                                                    #
#                 Using flat unsorted wordlist.                      #
#                                                                    #
######################################################################

Using flat unsorted wordlist.

The Wordlist contains  22633  words.
Building the Wordlist took 0.144 seconds

Enter a scrambled word (or EXIT):  fhist
Found  120 permutations;  120.0 unique permutations
Found word: shift
Solving this jumble took 0.08452 seconds
Checked  29  permutations.
Made  647913  comparisons.

Enter a scrambled word (or EXIT):  catex
Found  120 permutations;  120.0 unique permutations
Found word: exact
Solving this jumble took 0.15389 seconds
Checked  54  permutations.
Made  1219631  comparisons.

Enter a scrambled word (or EXIT):  dentr
Found  120 permutations;  120.0 unique permutations
Found word: trend
Solving this jumble took 0.15536 seconds
Checked  55  permutations.
Made  1222991  comparisons.

Enter a scrambled word (or EXIT):  tioid
Found  120 permutations;  60.0 unique permutations
Found word: idiot
Solving this jumble took 0.10211 seconds
Checked  35  permutations.
Made  790883  comparisons.

Enter a scrambled word (or EXIT):  shsal
Found  120 permutations;  60.0 unique permutations
Found word: slash
Solving this jumble took 0.13976 seconds
Checked  44  permutations.
Made  974272  comparisons.

Enter a scrambled word (or EXIT):  leyngt
Found  720 permutations;  720.0 unique permutations
Found word: gently
Solving this jumble took 0.61962 seconds
Checked  221  permutations.
Made  4981342  comparisons.

Enter a scrambled word (or EXIT):  trogof
Found  720 permutations;  360.0 unique permutations
Found word: forgot
Solving this jumble took 0.80773 seconds
Checked  288  permutations.
Made  6500317  comparisons.

Enter a scrambled word (or EXIT):  gewhit
Found  720 permutations;  720.0 unique permutations
Found word: weight
Solving this jumble took 0.37169 seconds
Checked  130  permutations.
Made  2934565  comparisons.

Enter a scrambled word (or EXIT):  yalelv
Found  720 permutations;  360.0 unique permutations
Found word: valley
Solving this jumble took 0.97888 seconds
Checked  342  permutations.
Made  7729655  comparisons.

Enter a scrambled word (or EXIT):  ounteg
Found  720 permutations;  720.0 unique permutations
Found word: tongue
Solving this jumble took 1.17410 seconds
Checked  410  permutations.
Made  9258831  comparisons.



######################################################################
#                                                                    #
#                      Using sorted wordlist.                        #
#                                                                    #
######################################################################

The Wordlist contains  22633  words.
Building the Wordlist took 13.952 seconds

Enter a scrambled word (or EXIT):  fhist
Found  120 permutations;  120.0 unique permutations
Found word: shift
Solving this jumble took 0.00045 seconds
Checked  29  permutations.
Made  420  comparisons.

Enter a scrambled word (or EXIT):  catex
Found  120 permutations;  120.0 unique permutations
Found word: exact
Solving this jumble took 0.00100 seconds
Checked  54  permutations.
Made  792  comparisons.

Enter a scrambled word (or EXIT):  dentr
Found  120 permutations;  120.0 unique permutations
Found word: trend
Solving this jumble took 0.00096 seconds
Checked  55  permutations.
Made  794  comparisons.

Enter a scrambled word (or EXIT):  tioid
Found  120 permutations;  60.0 unique permutations
Found word: idiot
Solving this jumble took 0.00048 seconds
Checked  35  permutations.
Made  510  comparisons.

Enter a scrambled word (or EXIT):  shsal
Found  120 permutations;  60.0 unique permutations
Found word: slash
Solving this jumble took 0.00074 seconds
Checked  44  permutations.
Made  629  comparisons.

Enter a scrambled word (or EXIT):  leyngt
Found  720 permutations;  720.0 unique permutations
Found word: gently
Solving this jumble took 0.00571 seconds
Checked  221  permutations.
Made  3219  comparisons.

Enter a scrambled word (or EXIT):  trogof
Found  720 permutations;  360.0 unique permutations
Found word: forgot
Solving this jumble took 0.00729 seconds
Checked  288  permutations.
Made  4184  comparisons.

Enter a scrambled word (or EXIT):  gewhit
Found  720 permutations;  720.0 unique permutations
Found word: weight
Solving this jumble took 0.00332 seconds
Checked  130  permutations.
Made  1884  comparisons.

Enter a scrambled word (or EXIT):  yalelv
Found  720 permutations;  360.0 unique permutations
Found word: valley
Solving this jumble took 0.00782 seconds
Checked  342  permutations.
Made  4923  comparisons.

Enter a scrambled word (or EXIT):  ounteg
Found  720 permutations;  720.0 unique permutations
Found word: tongue
Solving this jumble took 0.01112 seconds
Checked  410  permutations.
Made  5946  comparisons.


######################################################################
#                                                                    #
#                      Using hashed wordlist.                        #
#                                                                    #
######################################################################

Creating the Wordlist

The Wordlist contains 22633 words.
There are 1668 empty buckets
Non-empty buckets have an average length of 2.714 words
Building the Wordlist took 0.173 seconds

Enter a scrambled word (or EXIT):  fhist
Found word: shift
Solving this jumble took 0.00008 seconds
Made  3  comparisons.

Enter a scrambled word (or EXIT):  catex
Found word: exact
Solving this jumble took 0.00007 seconds
Made  1  comparisons.

Enter a scrambled word (or EXIT):  dentr
Found word: trend
Solving this jumble took 0.00007 seconds
Made  1  comparisons.

Enter a scrambled word (or EXIT):  tioid
Found word: idiot
Solving this jumble took 0.00013 seconds
Made  8  comparisons.

Enter a scrambled word (or EXIT):  shsal
Found word: slash
Solving this jumble took 0.00007 seconds
Made  1  comparisons.

Enter a scrambled word (or EXIT):  leyngt
Found word: gently
Solving this jumble took 0.00007 seconds
Made  1  comparisons.

Enter a scrambled word (or EXIT):  trogof
Found word: forgot
Solving this jumble took 0.00008 seconds
Made  1  comparisons.

Enter a scrambled word (or EXIT):  gewhit
Found word: weight
Solving this jumble took 0.00008 seconds
Made  4  comparisons.

Enter a scrambled word (or EXIT):  yalelv
Found word: valley
Solving this jumble took 0.00008 seconds
Made  1  comparisons.

Enter a scrambled word (or EXIT):  ounteg
Found word: tongue
Solving this jumble took 0.00007 seconds
Made  2  comparisons.