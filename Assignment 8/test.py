def insertionSort(lst, word):

    if len(lst) == 0:
        lst.append(word)
    else:
        for i in range (len(lst)):
            index = i
            if word < lst[i]:
                lst.insert(i+1, word)


                
lst = []

a = insertionSort(lst, "taylor")





