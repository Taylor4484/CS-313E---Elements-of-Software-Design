#Read File
openfile = open('myWordList.txt', 'r')

#Create wordList from content of read file
wordList = openfile.readlines()

#Clean the wordlist
cleanWordList = [line.strip().rstrip() for line in wordList]



#Set a default filename
defaultFile = 'myWordList.txt'

#Tell user the default filename
print('The default filename is [%s]' % defaultFile)

#Ask the user to accept default or type new filename
inputFileName = input("Hit 'Enter' to accept, or type new filename: ")

#Use defaultFile if no input, or use input
inputFileName = defaultFile or inputFileName
