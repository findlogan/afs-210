def ordered_binary_search(ordered_list, itemToBeFound):
    
    # Checking length of list, to see if we need to do anything
    if len(ordered_list) == 0:
        return False
    else:
        # Finding midpoint
        midpoint = len(ordered_list) // 2
        if ordered_list[midpoint] == itemToBeFound:
            return True
        else:
            # Use some divide and conquer to find which half and search through the ordered list
            if itemToBeFound < ordered_list[midpoint]:
                return binarySearch(ordered_list[:midpoint], itemToBeFound)
            else:
                return binarySearch(ordered_list[midpoint+1:], itemToBeFound)

def binarySearch(alist, itemToBeFound):

    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == itemToBeFound:
            found = True
        else:
            if itemToBeFound < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

print(ordered_binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
print(ordered_binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))