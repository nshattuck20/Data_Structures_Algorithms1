'''
Section 11.3
Example of linear search and binary search algorithms
1. Linear Search
    -Searches each element in the list until key is found or returns -1 if key not found.
2. Binary Search
    -Divides list in half, searching either lower up uppper sublists depending on the numerical/alphanumerical
    value of the key.
'''

def linear_search(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i
    return -1 # key not found
def binary_search(numbers, key):
    #Variables to hold low, mid, and high indices.
    #Starts with the entire range of the list.
    low = 0
    mid = len(numbers)//2
    high = len(numbers) - 1
    #Loop until low passes high
    while (high >= low):
        #calculate middle index
        mid = (high + low)//2
        #Cut the range to either left or right (low or high)
        #unless numbers[mid] is the key
        if (numbers[mid] < key):
            low = mid + 1
        elif(numbers[mid] > key):
            high = mid - 1
        else:
            return mid
    return - 1 # not found
def recursive_binary_search(numbers, low, high, key):
    if low > high:
        return - 1
    mid = (low + high)//2
    if numbers[mid] < key:
        return recursive_binary_search(numbers, mid+1, high, key)
    elif numbers[mid] > key:
        return recursive_binary_search(numbers, low, mid -1, key)
    return mid


#Main program to test linear_search(), binary_search(), and recursive_binary_searchO() functions
numbers = [2,4,7,10,11,32,45,87]
numbers.sort()
print('NUMBERS:', numbers)

key = int(input('Enter an integer value: '))
# key_index = linear_search(numbers, key)
# key_index = binary_search(numbers, key)
key_index = recursive_binary_search(numbers, 0, len(numbers), key)
if(key_index == -1):
    print('%d was not found' % key)
else:
    print('Found %d at index %d' % (key, key_index))

