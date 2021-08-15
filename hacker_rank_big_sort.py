def bigSorting(unsorted):
    for j in range(len(unsorted)):
        for i in range(len(unsorted)):
            if unsorted[j] < unsorted[i]:
                (unsorted[j],unsorted[i]) = (unsorted[i],unsorted[j])
    return unsorted


#EXAMPLE 
print(bigSorting([6,31415926535897932384626433832795,1,3,10,3,5]))
