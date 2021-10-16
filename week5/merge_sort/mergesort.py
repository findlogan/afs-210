def mergeSort(alist):
    print("Splitting ",alist)

    # The length of the list is more than 1..
    if len(alist)>1:

        # Finding middle of a list
        middleOfList = len(alist)//2
        leftHalf = alist[:middleOfList]
        rightHalf = alist[middleOfList:]
        
        # Run mergesort for each half
        # This is ran recursively
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=j=k=0       
        # This loop will continue to run if i counter and j counter is less than the length of the halves
        while i < len(leftHalf) and j < len(rightHalf):
            
            # if the leftHalf[i] is less than righthalf[j] number
            if leftHalf[i] < rightHalf[j]:

                # Put the left half in position k
                alist[k]=leftHalf[i]

                # Left half increments by 1
                i = i + 1
            else:

                # Otherwise, the right half is actually smaller, so it needs to go in position k
                alist[k]=rightHalf[j]

                # Right half increments by 1
                j = j + 1

            # Increment k index by 1
            k=k+1

        # While i counter is less than length of left half,
        while i < len(leftHalf):

            # alist at index [k] will now be leftHalf index [i]
            alist[k]=leftHalf[i]

            # Increment both indexes by 1
            i = i + 1
            k = k + 1
        
        # While index j is less than the length of the right half,
        while j < len(rightHalf):

            # alist at index[k] will now be right half index [j] number
            alist[k]=rightHalf[j]

            # increment both
            j = j + 1
            k = k + 1
    print("Merging ",alist)

# Provide a list, and run merge sort to show the re-ordering of the list.
alist = [14,46,43,27,57,41,45,21,70]
mergeSort(alist)
print(alist)