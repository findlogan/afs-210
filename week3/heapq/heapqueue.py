import heapq

numbers = [25, 35, 22, 85, 14, 65, 75, 22, 58]

largest_numbers = heapq.nlargest(3, numbers)

print("Original List:")
print(numbers)

print("Three largest numbers are:", largest_numbers)