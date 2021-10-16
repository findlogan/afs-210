# In the counting sort, you provide a list and the highest value that is in that list
def counting_sort(alist, max_val):

    # m is going to be the maximum value + 1
    m = max_val + 1
    count = [0] * m                
    
    for x in alist:
    # count occurences of x number in alist
        count[x] += 1             
    i = 0

    # For each number in the range of max val + 1
    for x in range(m):            
        
        # For each occurance of X in the range
        for c in range(count[x]):  
            
            # Set the current index equal to the number we're currently looking at
            alist[i] = x
            # Increment i for the index for next number
            i += 1
    
    # When done, return the sorted list back with all the numbers
    return alist

print(counting_sort( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))