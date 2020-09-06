'''
A look at a binary search through a list of numbers.
Note that the list needs to be sorted in order for
a binary search to perform.
'''

def BinarySearch(numbers, low, high, key):
    if (low > high):
        return -1
    mid = (low + high) // 2
    if(numbers[mid] < key): # If the key index is > mid
        return BinarySearch(numbers, mid + 1, high, key)
    elif (numbers[mid] > key): # If the key index is < mid
        return BinarySearch(numbers, low, mid-1, key)
    return mid

numbers = [14,26,42,59,71,88,92]
print(BinarySearch(numbers, 0, len(numbers), 42))