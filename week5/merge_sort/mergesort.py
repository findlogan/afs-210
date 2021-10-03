def mergeSort(alist):
    print("Splitting ",alist)

    # The length of the list is more than 1..
    if len(alist)>1:

        # Finding middle of a list
        middleOfList = len(alist)//2
        leftHalf = alist[:middleOfList]
        rightHalf = alist[middleOfList:]
        
        # Run mergesort for each half
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        i=j=k=0       
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                alist[k]=leftHalf[i]
                i = i + 1
            else:
                alist[k]=rightHalf[j]
                j = j + 1
            k=k+1

        while i < len(leftHalf):
            alist[k]=leftHalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):
            alist[k]=rightHalf[j]
            j = j + 1
            k = k + 1
    print("Merging ",alist)

# Provide a list, and run merge sort to show the re-ordering of the list.
alist = [14,46,43,27,57,41,45,21,70]
mergeSort(alist)
print(alist)