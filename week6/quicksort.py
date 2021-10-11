import time
import random


# Original Sample with Beginning Pivot Point:

def beginning_pivot_quick_sort(arr, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the beginning_pivot_partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = beginning_pivot_partitionStart(arr, start, end)
    beginning_pivot_quick_sort(arr, start, pivot-1)
    beginning_pivot_quick_sort(arr, pivot+1, end)
        

def beginning_pivot_partitionStart(arr, start, end):
    return beginning_pivot_partition(arr, start, end)

def beginning_pivot_partition(arr, start, end):
    # Select the first element as our pivot point
    pivot = arr[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and arr[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and arr[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            arr[low], arr[high] = arr[high], arr[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    # Swap the values
    arr[start], arr[high] = arr[high], arr[start]

    return high


# Pivot point using the end (alt 1)

def ending_partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def ending_quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        partionIndex = ending_partition(arr, low, high)

        # Sorting elements sperately before and after the partition
        ending_quickSort(arr, low, partionIndex-1)
        ending_quickSort(arr, partionIndex+1, high)


# Using a random point as the pivot point (alt 2)

def random_quicksort(arr, start , stop):
    if(start < stop):

        # This variable, pivotindex is where the pivot is within the array
        pivotindex = random_partition(arr, start, stop)

        # The array is partially sorted around the pivot point
        # Sort the left half of the array, and the right half seperately.
        random_quicksort(arr , start , pivotindex-1)
        random_quicksort(arr, pivotindex + 1, stop)

# This picks a random pivoting point. It swaps the first element with the pivot, and then calls the partion function
def random_partition(arr , start, stop):

    # Generate the random number between the starting index, and the ending index of the array.
    randpivot = random.randrange(start, stop)

    # Swap the starting element of the array and the pivot
    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition_random(arr, start, stop)

# This takes the first element as a pivot, and then places the pivot at the correct position
# Everything is arranged according to the pivot, and everything smaller than the pivot is on the left, and the greater on the right.
def partition_random(arr,start,stop):
    pivot = start # pivot

    # Variable to remember where the partion array starts from
    i = start + 1

    for j in range(start + 1, stop + 1):
            
        # if the current element is smaller or equal to the pivot, shift it to the left side of the partition
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)

# median as a pivot point (alt 3)
def middle_partition(arr, low, high):
    pivot = arr[(low + high) // 2]

    i = low - 1 # index of the smaller element
    j = high + 1 # index of the higher element

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j

        #If element on left side of pivot (i) is larger than the element on the right (j), then swap them.
        arr[i], arr[j] = arr[j], arr[i]


    # Create a helper function that will be called recursively
def middle_quicksort(items, low, high):
    if low < high:
        # This is the index in the array after the pivot, this is where we will split out list
        arrSplit = middle_partition(items, low, high)
        middle_quicksort(items, low, arrSplit)
        middle_quicksort(items, arrSplit + 1, high)


# ----
# Outputs
# ---


myList = [x for x in range(1000)]

# myList = [54,26,93,17,77,31]

# Shuffle the list, so that it has something to sort.
random.shuffle(myList)



# Beginning pivot point (sample code)

# print("Beginning Pivot Quick Sort at the beginning:")
# print(myList)
print ('Performing Beginning Pivot Point Quick Sort')
start_time = time.time()
beginning_pivot_quick_sort(myList, 0, len(myList)-1)
end_time = time.time()
print(f"The execution time is: {end_time-start_time}")
# print ("Beginning Pivot Quick Sort at the End:")
# print(myList)   

random.shuffle(myList)

# Ending pivot point (alt 1)

# print("Ending Pivot Quick Sort at the beginning:")
# print(myList)
print ('Performing Ending Pivot Point Quick Sort')
start_time = time.time()
ending_quickSort(myList, 0, len(myList) - 1)
end_time = time.time()
print(f"The execution time is: {end_time-start_time}")
# print ("Ending Pivot Quick Sort at the End:")
# print(myList)   

random.shuffle(myList)

# Random pivot point (alt 2)

# print("Random Pivot Quick Sort at the beginning:")
# print(myList)
print ('Performing Random Pivot Point Quick Sort')
start_time = time.time()
random_quicksort(myList, 0, len(myList) - 1)
end_time = time.time()
print(f"The execution time is: {end_time-start_time}")
# print ("Random Pivot Quick Sort at the End:")
# print(myList)   

random.shuffle(myList)

# median as a pivot point (alt 3)
# print("Median Pivot Quick Sort at the beginning:")
# print(myList)
print ('Performing Median Pivot Point Quick Sort')
start_time = time.time()
middle_quicksort(myList, 0, len(myList) - 1)
end_time = time.time()
print(f"The execution time is: {end_time-start_time}")
# print ("Median Pivot Quick Sort at the End:")
# print(myList)   