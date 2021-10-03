def counting_sort(alist, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for x in alist:
    # count occurences of x in alist
        count[x] += 1             
    i = 0
    for x in range(m):            
        for c in range(count[x]):  
            alist[i] = x
            i += 1
    
    # When done, return the sorted list back with all the numbers
    return alist

print(counting_sort( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))